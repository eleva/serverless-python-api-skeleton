from dotenv import load_dotenv
import json
import mysql.connector
import os

load_dotenv()

db = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_DATABASE")
)

def hello(event, context):

    #Fake select just to demonstrate mysql connection is working
    cursor = db.cursor()
    cursor.execute("SELECT 'Go Serverless v3.0! Your function executed successfully!'")
    result = cursor.fetchall()

    #Prepare body
    body = {
        "message": result[0][0],
        "input": event
    }

    #Prepare response
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
