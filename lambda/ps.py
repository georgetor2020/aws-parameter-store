import boto3
import os
import json
import mysql.connector

ps = boto3.client('ssm')

db = "DevDB"

# Initialize SQL Endpoint, Port, and Parameter Store values from environment
environment = os.environ.get('Environment', 'Dev')
parameterRoot = os.environ.get('ParamRoot', '/mydb') + "/" + environment
host = os.environ.get('MySQLEndpoint', " devdbcluster-ps.cluster-cjdii2k9xlvv.us-east-2.rds.amazonaws.com ")
port = os.environ.get('MySQLPort', "3306")

print("host:", host)

# Get the login from parameter store
login = ""
password = ""
try:
   param = parameterRoot + "/Login"
   print("calling get_parameter with parameter {}".format(param))
   login = ps.get_parameter(Name=param)['Parameter']['Value']
   # print("login: ", login)
   
   param = parameterRoot + "/Password"
   print("calling get_parameter with parameter {}".format(param))
   password = ps.get_parameter(Name=param)['Parameter']['Value']
   # print("password: ", password)

except Exception as e:
   print("unknown exception", e)
   exit(1)

# Connect to MySQL
try:
   mydb = mysql.connector.connect(
      host=host,
      user=login,
      database=db,
      password=password
   )
except Exception as e:
   print("error connecting to MySql: ", e)
   exit(2)


def lambda_handler2(event, context):
   print("Hello from Lambda!")
   return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
   }


def lambda_handler(event, context):
   # print("event: ",event,"\n","-"*20)
   result = {"Error": "SQL Failed"}
   SQL = "SELECT * FROM customer LIMIT 10"
   try:
      mycursor = mydb.cursor()

      mycursor.execute(SQL)

      myresult = {}
      myresult["body"] = mycursor.fetchall()
      myresult["StatusCode"] = 202
      result = json.dumps(myresult)
      result = myresult
      # result = myresult
   except Exception as e:
      print("error executing SQL: ", SQL, " : ", e)
   return (result)

# if __name__ == '__main__':
#    r = lambda_handler(event="",context="")
#    print(r)
