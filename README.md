# Parameter Store workshop

## Overview


_AWS Systems Manager Parameter Store_ and _AWS Secrets Manager_ provide secure, highly available storage for configuration data and secrets.  You can store values as plaintext (unencrypted data) or ciphertext (encrypted data). You can then reference values by using the unique name that you specified when you created the parameter. Highly scalable, available, and durable, Parameter Store is backed by the AWS Cloud.

In this lab, we will focus on the basics of Parameter Store.



### Requirements

* AWS account - if you're doing this workshop as a part of an AWS event, you will be provided an account through a platform called Event Engine. The workshop administrator will provide instructions. If the event specifies you'll need your own account or if you're doing this workshop on your own, it's easy and free to [create an account](https://aws.amazon.com/) if you do not have one already.
* If using your own AWS account, We haven't finished the setup documentation.

Familiarity with AWS, Python, CloudFormation, EC2, and Lambda is a plus but not required.

### What you'll do

The labs in the workshop are designed to be completed in sequence, and the full set of instructions are documented in each lab.  Read and follow the instructions to complete each of the labs.  Don't worry if you get stuck, we provide hints along the way.

* **[Lab 1](lab1):** Add your Secrets to Parameter Store
* **[Lab 2](lab2):** Create an Aurora Serverless MySQL cluster
* **[Lab 3](lab3):** Verify that you can access your data with AWS Lambda

### Conventions

#### 1. Commands

Throughout this workshop, we will provide commands for you to run in a terminal. These commands will look like this:

<pre>
  ssh -i <b><i>PRIVATE_KEY.PEM</i></b> ec2-user@<b><i>EC2_PUBLIC_DNS_NAME</i></b>
</pre>


#### 2. Hints

Hints are also provided along the way and will look like this:

<details>
<summary>HINT</summary>

**Nice work, you just revealed a hint!**
</details>

*Click on the arrow to show the contents of the hint.*

#### 3. Details

If you are curious, there are a few sections of the lab which you by expanding the >details link
<details><summary>details</summary>

``` 
	print('More content is in the details, typically things like code fragments which may not be of general interest.')
```

</details> 

### IMPORTANT: Workshop Cleanup

If you're attending an AWS event and are provided an account to use, you can ignore this section because we'll destroy the account once the workshop concludes. Feel free to proceed to [lab1](lab1).

**If you are using your own account**, it is **VERY** important you clean up resources created during the workshop. Follow these steps once you're done going through the workshop to delete resources that were created:

1. Delete any manually created assets - for example:
	  * Remove Cloud9 from the database security group from lab1
2. Navigate to the [CloudFormation dashboard](https://console.aws.amazon.com/cloudformation/home#/stacks) in the primary region and click on your workshop stack name to load stack details.
3. Click **Delete** to delete the stack.

<details>
<summary>Troubleshooting: Stack delete failed</summary>
The Lambda function was created in a private VPC.  To delete this, CloudFormation needs to delete the ENIs associated with the Lambda function. It may take longer than expected to delete this stack, please be patient.

</details>

* * *

## Let's Begin!

[Go to Lab1 to start learning about parameter store](lab1)

## Participation

We encourage participation; if you find anything, please submit an [issue](https://github.com/dotstar/parameter-store/issues). However, if you want to help raise the bar, submit a [PR](https://github.com/dotstar/parameter-store/pulls)!
