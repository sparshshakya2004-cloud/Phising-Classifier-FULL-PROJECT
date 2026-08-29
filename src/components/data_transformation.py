import sys
import os 
import pandas as pd 
import numpy as np 
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler , FunctionTransformer , StandardScaler , OneHotEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import RandomOverSampler

from src.constant import *
from src.exception import CustomException
from src.utils.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    data_transformation_dir = os.path.join(artifact_folder, 'data_transformation')
    transformed_train_file_path = os.path.join(data_transformation_dir , 'train.npy')
    transformed_test_file_path = os.path.join(data_transformation_dir , 'test.npy')
    transformed_object_file_path = os.path.join(data_transformation_dir, 'preprocessing')

class DataTransformation:

    def __init__(self , valid_data_dir):
        self.valid_data_dir = valid_data_dir
        self.transformation_config = DataTransformationConfig()
        self. MainUtils()

    @staticmethod
    def get_merged_batch_data(valid_data_dir : str) -> pd.DataFrame:
        """
        Method Nmae : get_merged_batch_data
        Description : This method reads all the validated raw data from the

        OUTPUT      : a pandas Data Frame Contaning the merged data
        On Failure  : Write an exception log and then raise an exception

        version     : 1.2
        Revisions   : moved setup to cloud 
        """
        try:
            raw_files = os.listdir(valid_data_dir)
            csv_data = []
            for filename in raw_files:
                data = pd.read_csv(os.path.join(valid_data_dir , filename))
                csv_data.append(data)
            merged_data = pd.concat(csv_data)
            return merged_data
        except Exception as e :
            raise CustomException(e,sys)

    def initiate_data_transformation(self):
        """
        Method Name : initiate_data_transformation
        Description : This  method initiates the data transformation component for the pipeline

        Output      : data transformation artifact is created and returned
        On Failture : write an exception log and then raise an exception

        version     : 1.2
        revision    : moved setup to cloud 
        """
        logging.info(
            "Entered initiate_data_transformation method of Data_Transformation class"
        )

        try : 
            dataframe = self.get_merged_batch_data(valid_data_dir= self.valid_data_dir)
            dataframe = self.utils.remove_unwanted_spaces(dataframe)
            dataframe.replace('?' , np.NaN , inplace = True)

            X = dataframe.drop(columns = TARGET_COLUMN)
            y = np.where(dataframe[TARGET_COLUMN] == -1,0,1)

            sampler = RandomOverSampler()
            x_sampled , y_sampled = sampler.fit_resample(X,y)

            x_train , x_test , y_train , y_test = train_test_split(x_sampled , y_sampled)

            preprocessor = SimpleImputer(strategy='most_frequent')

            x_train_scaled = preprocessor.fit_transform(x_train)
            x_test_scaled = preprocessor.transform(x_test)

            preprocessor_path = self.data_transformation_config.transformed_object_file_path
            os.makedirs(os.path.dirname(preprocessor) , exist_ok= True)
            self.utils.save_object(file_path = preprocessor_path , obj = preprocessor)

            return x_train_scaled , y_train , x_test_scaled , y_test, preprocessor_path

        except Exception as e :
            raise CustomException(e , sys) from e
