import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation , DataTransformationConfig
from src.components.model_trainer import ModelTrainer , ModelTrainerConfig
from src.utils import save_object,evaluate_models

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")   # artifacts is basically the folder 


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
        
            df = pd.read_csv('notebook\data\stud.csv')   # read the student csv file 
            logging.info("Data ingestion successful")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok=True)  # if already presnt do not add any new

            # to save the raw data path
            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)  

            logging.info("Train test split execution started")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False , header=True)  # save the train data in the train.csv file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False , header=True)  # save the test data similarly


            logging.info(" Ingestion successful")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e , sys)


if __name__=="__main__":

    # first done the data ingestion 
    obj = DataIngestion()
    trains_data , test_data = obj.initiate_data_ingestion()
    
    # then do the data transformation
    data_transformation = DataTransformation()
    train_array , test_array , _ = data_transformation.initiate_data_transformation(trains_data , test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_array , test_array))