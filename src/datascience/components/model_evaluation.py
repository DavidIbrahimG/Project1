import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
from pathlib import Path
from src.datascience.config.configuration import ModelEvaluationConfig
from src.datascience.utils.common import save_json
import mlflow.sklearn
import numpy as np
import joblib

"""import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/DavidIbrahimG/Project1.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "DavidIbrahimG"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "57784cd3735838b36046f55be85608fe82144f40"
"""


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run() as run:

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            ## saving metrics as local 
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            ## logging params in MLflow
            mlflow.log_params(self.config.all_params)

            ## logging metrics in MLflow
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            ## model registry does not work with file store
            """if tracking_uri_type_store != "file":
                # Log the model to the remote server and register it
                mlflow.sklearn.log_model(model, "model", registered_model_name="model")
            else:
                # Log the model to the local file system (no model registration)
                mlflow.sklearn.log_model(model, "model")"""
