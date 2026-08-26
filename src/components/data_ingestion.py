import sys
import os 
import numpy as np
import pandas as pd 
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging

from src.data_access.phising_data import PhisingData
from src.utils.main_utils import MainUtils
from dataclasses import dataclass