import boto3
# from botocore.exceptions import ParameterNotFound
import os
import json
import mysql.connector

ps = boto3.client('ssm', region_name='us-east-2')

environment = os.environ.get('Environment', 'Dev')
parameterRoot = os.environ.get('ParamRoot', '/mydb') + "/" + environment
host = os.environ.get('MySQL-Endpoint', " devdbcluster-ps.cluster-cjdii2k9xlvv.us-east-2.rds.amazonaws.com ")
port = os.environ.get('MySQL-Port', "3306")

# Get the login from parameter store
login = ""
password = ""
try:
   login = ps.get_parameter(Name=(parameterRoot + "/Login"))['Parameter']['Value']
   print("login: ", login)
   password = ps.get_parameter(Name=(parameterRoot + "/Password"))['Parameter']['Value']
   print("password: ", password)
except Exception as e:
   print("unknown exception", e)
   exit(1)

# Connect to MySQL
mydb = mysql.connector.connect(
   host=host,
   user=login,
   password=password
)
print(mydb)


def lambda_handler(event, context):
   # print("Received event: " + json.dumps(event, indent=2))
   print("value1 = " + event['key1'])
   print("value2 = " + event['key2'])
   print("value3 = " + event['key3'])
   return event['key1']  # Echo back the first key value
   # raise Exception('Something went wrong')

# if __name__ == '__main__':
# print(myparams)
# r = ps.get_parameter(Name=myparams)
# p = json.loads(r['Parameter']['Value'])
# print(p)
# login = p['Login']
# password = p['Password']
# print('login: ',login)
# print('password:',password)
