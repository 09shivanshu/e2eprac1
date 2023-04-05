import os

class TrainingPipelineConfig:
    
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),f"{datetime.now().strftime('%m%d%y__%h%m%s')})

class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
