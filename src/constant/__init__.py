from datetime import datetime
import os 

AWS_S3_BUCKET_NAME = "phishingclassifierbucket"
MONGO_DATABASE_NAME = "phising-classifier"

TARGET_COLUMN = "Result"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
artifact_folder = os.path.join("artifacts" , artifact_folder_name)


MONGO_USERNAME='sparshshakya2004_db_user'
MONGO_PASSWORD='JY09CWtnommoOwHO'
MONGO_HOST='cluster0.arbefhm.mongodb.net'
MONGO_DATABASE='phising-classifier'