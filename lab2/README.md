# Parameter Store workshop


## Workshop progress

✅[Lab 1: Add your secrets to Parameter Store](../lab1)

**Lab 2: Create an Aurora Serverless MySQL cluster**

[Lab 3: Access Parameters from your code](../lab3)


## Lab 2: Create an Aurora Serverless MySQL cluster

In this lab, we will modify a CloudFormation template to use the parameters you just edited.

## 1. Setup CloudFormation Template

In this first lab, we will create a Serverless MySQL database using our _Dev_ parameters.  We need to edit the CloudFormation template file, ~/environment/parameter-store/lab2/aurora.yaml.

<details>
We could have used any database, or other AWS service which requires credentials or configuration detail.  

The lab is using a Serverless version of Aurora for it's unique ability to scale to 0.  With Serverless Aurora, after a period of time when there are no connections to the database, it shutsdown.  This is particularly interesting for a development or lab database, as it is very cost effective.  When the database is down, you pay for just the storage used.  It's a simple, cost-effective option for infrequent, intermittent, or unpredictable workloads.

When a connection is received, the database restarts.  The database restart time is elongated, typically between 20 and 40 seconds.  After this one "cold start", connection times are comparable with other MySQL databases.
</details>


One way to do this in cloud9, is to navigate to lab2 in Cloud9's left panel, and double click on the file named **aurora.yaml.**

<div align="center">



![Cloud9 Edit Navigation](./img/1.png).

</div>

Edit the template parameter named “ParameterRoot”.  Set the Default value to the root of your parameter store _/mydb_).

<div align="center">

![Cloud9 Edit](./img/2.png)

</div>

Note that the following two template parameters have been pre-populated to set variables DevPass and DevLogin from the Parameter Store.

Save the CloudFormation template, and create a stack.  The stack will create an Aurora MySQL serverless database, and a lambda function.  We’ll come back to the lambda in the next lab.

## 1. 2.	Create the database, using CloudFormation

We will invoke CloudFormation from the CLI.

Issue the commands to create a CloudFormation stack:

<pre>
cd ~/environment/parameter-store/lab2

aws cloudformation create-stack --stack-name rds-ps --template-body file://aurora.yaml --capabilities CAPABILITY_NAMED_IAM

</pre>

The CLI returns output similar to:
```
{
    "StackId": "arn:aws:cloudformation:us-east-1:233363133948:stack/rds-ps/e3a1a080-3259-11ea-a41e-0af77bd56d08"
}

```
<div align="center">

![Cloud9 IDE](../img/4.png)
</div>
When Cloud9 initializes, it will *automatically* download the github content from https://github.com/dotstar/parameter-store.

Time to initialize our parameters.  We are going to create a MySQL database with administrative access provided by Parameter Store.

## 2. Create Parameters

Here is the hierarchy of parameters we will create.

<div align="center">

![Parameter Hierarcy](../img/5.png)

</div>

One would normally type in parameters one at a time, from the GUI, CLI, API, or CloudFormation.  For this lab, there is a helper script to speed things up a bit.

In the command line of Cloud9, run the helper script.

<details>
<summary>HINT</summary>

**Press ALT-t to open a larger terminal window**
</details>


<pre>
  cd ~/environment/parameter-store/lab1
  python init-parms.py
</pre>

The expected output from running these commands:
```
here are your parameters, from the parameter store:
[  {  'ARN': 'arn:aws:ssm:us-east-1:233363133948:parameter/mydb/Dev/Login',
      'LastModifiedDate': datetime.datetime(2020, 1, 8, 20, 0, 28, 944000, tzinfo=tzlocal()),
      'Name': '/mydb/Dev/Login',
      'Type': 'String',
      'Value': 'admin',
      'Version': 2},
   {  'ARN': 'arn:aws:ssm:us-east-1:233363133948:parameter/mydb/Dev/Password',
      'LastModifiedDate': datetime.datetime(2020, 1, 8, 20, 0, 28, 987000, tzinfo=tzlocal()),
      'Name': '/mydb/Dev/Password',
      'Type': 'String',
      'Value': 'CHANGE-ME-NOW',
      'Version': 3},
   {  'ARN': 'arn:aws:ssm:us-east-1:233363133948:parameter/mydb/Prod/Login',
      'LastModifiedDate': datetime.datetime(2020, 1, 8, 20, 0, 29, 66000, tzinfo=tzlocal()),
      'Name': '/mydb/Prod/Login',
      'Type': 'String',
      'Value': 'admin',
      'Version': 2},
   {  'ARN': 'arn:aws:ssm:us-east-1:233363133948:parameter/mydb/Prod/Password',
      'LastModifiedDate': datetime.datetime(2020, 1, 8, 20, 0, 29, 105000, tzinfo=tzlocal()),
      'Name': '/mydb/Prod/Password',
      'Type': 'String',
      'Value': 'CHANGE-ME-NOW',
      'Version': 2}]

```

<details>
Here our helper script code.  

It parses values from a JSON input file and calls put_parameter() to copy these values to Parameter store.  

Note the use of a hierarchy of parameters.  There is on tree for _Pub_ and a seperate one for _Dev_ instances.  In the real world, we would likely have different permissions for each of these paths, so that the whole world wouldn't have access to production credentials.

```
import boto3
from pprint import pprint
import json


inputfile = "parameters.json"
topkey = '/mydb'
ps = boto3.client('ssm',region_name='us-east-1')


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
   r = ps.get_parameters_by_path(
      Path=topkey,
      Recursive=True,
      MaxResults=10
   )
   print('here are your parameters, from the parameter store:')
   pprint(r['Parameters'],indent=3)

````
</details>

## 3. Change a Parameter

Let's change the value of the development database password in Parameter Store.  We will use the GUI, but of course you could do this via API or CloudFormation, if desired.

Navigate to the parameter store service.  Parameter store is part of AWS System Manager.  From the console, you can enter "parameter" or "ssm" or "systems manager".
<div align="center">

![Systems Manager Parameter Store Console Search](./img/1.png)

 

![Systems Manager Parameter Store Console ](./img/2.png)
</div>

For this workshop, we will build an Aurora Serverless Database from Cloudformation.  Cloudformation will obtain the administrative credentials from Parameter store.
Select the Parameter /mydb/Dev/Password and edit the password.  Save it when you are complete, and don’t forget what you typed.  You will use it later.

**Be certain that the password complies with MySQL requirements.  By the default, the constraints on the master password are: _At least 8 printable ASCII characters. Can't contain any of the following: / (slash), "(double quote) and @ (at sign)_**

<div align="center">

![Edit Parameter ](./img/3.png)


![Edit Parameter Value ](./img/4.png)

</div>

## 4. Check your work

Return to the CLI (in Cloud9) , inspect parameter store to validate that the login and password are as you set them.  From the CLI, issue the _ssm_ command to view a path of parameters.

<pre>
  aws ssm get-parameters-by-path --path /mydb --recursive
</pre>

When you are satisfied that you’ve changed the Dev password, proceed to [lab2](../lab2), creating a database

### Checkpoint

Congratulations!!!  You've successfully added parameters and edited the default administrative password. On to the next lab!

Proceed to [Lab 2](../lab2)!

[*^ back to top*](#lab1)

## Participation

We encourage participation; if you find anything, please submit an [issue](https://github.com/dotstar/parameter-store/issues). However, if you want to help raise the bar, submit a [PR](https://github.com/dotstar/parameter-store/pulls)!

<!--## License

This library is licensed under the Apache 2.0 License.
-->