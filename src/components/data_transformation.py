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