
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact





class DataValidation:
    

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact
                 ):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys)from e
        
    
    def is_train_test_file_exist(self):
        try:
            logging.info("started if training and testing is available")
            is_train_file_exist=False
            is_test_file_exist=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            is_available= is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists?->{is_available}")

            return is_available


        except Exception as e:
            raise HousingException(e,sys) from e
        


    def validate_dataset_schema(self)->bool:
        try:
            validation_status=False

            validation_status=True
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self):
        try:
            is_available=self.is_train_test_file_exist()

            if not is_available:
                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Training File:{training_file} or testing file :{testing_file}"\
                "is not present"
                logging.info(message)
                raise Exception(message)
            
            validation_status=self.validate_dataset_schema()
            
            

        except Exception as e:
            raise HousingException(e,sys)from e
        


