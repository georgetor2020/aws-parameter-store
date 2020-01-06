import boto3
from pprint import pprint
import json


inputfile = "secrets.json"
topkey = '/mydb'
ps = boto3.client('ssm',region_name='us-east-2')


if __name__ == '__main__':
   with open(inputfile,"r") as myfile:
      data = myfile.read()
   obj = json.loads(data)
   # print (obj)

   # Initialize Parameters for Dev
   try:
      for env in ['Dev','Prod']:
         # Put login information into parameter store
         ps.put_parameter(
            Name = topkey + '/' + env + '/'+ 'Login',
            Description = "Login for " + env + "MyDB",
            Value = obj[env]['Login'],
            Type = 'String',
            Overwrite = True
         )
         # Put password information into parameter store
         ps.put_parameter(
            Name = topkey + '/' + env + '/'+ 'Password',
            Description="Password for " + env + "MyDB",
            Value = obj[env]['Password'],
            Type = 'String',
            Overwrite=True
         )
   except Exception as e:
      print(e)
      print('exiting')
      exit

   print('contents of {} key in parameter store:'.format(topkey))
   r = ps.describe_parameters(
      Filters=[
         {
            'Key': 'Name',
            'Values': [topkey,]
         }
      ]
   )
   pprint(r['Parameters'],indent=3)

