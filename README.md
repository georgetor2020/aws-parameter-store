# Parameter Store workshop

## Overview
![welcome](/img/1.png)


AWS Systems Manager Parameter store and AWS Secrets Manager provide secure, storage for configuration data and secrets management.  You can store values as plaintext (unencrypted data) or ciphertext (encrypted data). You can then reference values by using the unique name that you specified when you created the parameter. Highly scalable, available, and durable, Parameter Store is backed by the AWS Cloud. 

In this lab, we will focus on the basics of Parameter Store.



### Requirements

* AWS account - if you're doing this workshop as a part of an AWS event, you will be provided an account through a platform called Event Engine. The workshop administrator will provide instructions. If the event specifies you'll need your own account or if you're doing this workshop on your own, it's easy and free to [create an account](https://aws.amazon.com/) if you do not have one already.
* If using your own AWS account, create and use an IAM account with elevated privileges. Easiest option is to create an IAM user with admin privileges.

Familiarity with AWS, Python, Cloudformation, and Lambda is a plus but not required.

### What you'll do

The labs in the workshop are designed to be completed in sequence, and the full set of instructions are documented in each lab. Read and follow the instructions to complete each of the labs. Don't worry if you get stuck, we provide hints along the way.

* **[Lab 1](lab-1-parameterstore):** Add your Secrets to Parameter Store
* **[Lab 1](lab-1-cloudformation):** Deploy Cloudformation template which uses these secrets for an Aurora Serverless MySQL cluster
* **[Lab 2](lab-2-cli):** Verify that you can access your database from the CLI
* **[Lab 3](lab-2-lambda):** Verify that you can access your AWS Lambda

### Conventions

#### 1. Commands

Throughout this workshop, we will provide commands for you to run in a terminal. These commands will look like this:

<pre>
$ ssh -i <b><i>PRIVATE_KEY.PEM</i></b> ec2-user@<b><i>EC2_PUBLIC_DNS_NAME</i></b>
</pre>

The command starts **after** the $.

#### 2. Unique values

If you see ***UPPER_ITALIC_BOLD*** text, that means you need to enter a value unique to your environment. For example, the ***PRIVATE\_KEY.PEM*** above refers to the private key of an SSH key pair that's specific to your account; similarly, the ***EC2_PUBLIC_DNS_NAME*** refers to the DNS name of an EC2 instance in your account.

All unique values required throughout the workshop are captured as outputs from the CloudFormation template you'll launch to set up the workshop environment. You can, of course, also visit the specific service's dashboard in the [AWS management console](https://console.aws.amazon.com).

#### 3. Specific values or text

If you are asked to enter a specific value or text, it will formatted like this - `verbatim`.

#### 4. Hints

Hints are also provided along the way and will look like this:

<details>
<summary>HINT</summary>

**Nice work, you just revealed a hint!**
</details>

*Click on the arrow to show the contents of the hint.*

### IMPORTANT: Workshop Cleanup

If you're attending an AWS event and are provided an account to use, you can ignore this section because we'll destroy the account once the workshop concludes. Feel free to proceed to [Lab-0 to get started](lab-0-init).

**If you are using your own account**, it is **VERY** important you clean up resources created during the workshop. Follow these steps once you're done going through the workshop to delete resources that were created:

1. Delete any manually created assets - for example:
      * DynamoDB Global Tables replica from lab 3
      * Global Accelerator from lab 4
2. Navigate to the [CloudFormation dashboard](https://console.aws.amazon.com/cloudformation/home#/stacks) in the primary region and click on your workshop stack name to load stack details.
3. Click **Delete** to delete the stack.
4. Repeat steps 2-3 for the secondary region.

<details>
<summary>Troubleshooting: Stack delete failed</summary>
There are helper Lambda functions that should clean things up when you delete the main stack. However, if there's a stack deletion failure due to a race condition, follow these steps:

1. In the CloudFormation dashboard, click on the **Events** section, and review the event stream to see what failed to delete
2. Manually delete those resources by visiting the respective service's dashboard in the management console
3. Once you've manually deleted the resources, try to delete the main workshop CloudFormation stack again. Repeat steps 1-3 if you still see deletion failures

</details>

* * *

## Let's Begin!

[Go to Lab-0 to set up your environment](lab-0-init)

## Participation

We encourage participation; if you find anything, please submit an [issue](https://github.com/dotstar/parameter-store/issues). However, if you want to help raise the bar, submit a [PR](https://github.com/aws-samples/aws-multi-region-bc-dr-workshop/pulls)!