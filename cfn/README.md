# Parameter Store workshop


## Workshop progress

## Lab 0: Build the VPC

<div align="center">

#Only do this part if you are running in your own AWS account.  If you are at an AWS event, using _Event Engine_ this will fail.

</div>

If you are here, you need to setup the VPC, prior to running the Parameter store lab.  There is a CloudFormation template which will do all of the heavy lifting.  Here are the steps:

<pre>
cd /tmp
git pull https://github.com/dotstar/parameter-store.git
cd parameter-store/cfn
make create
</pre>

The template creates a VPC with 3 layers.  There are two public, two private, and three database subnets.  It adds NAT Gateways, Route Tables, and the other pieces need to perform the lab.

It also creates a Cloud9 instance, from which we run the remainder of the lab.

Please allow the stack to complete, then join [lab1](lab1).


## Participation

We encourage participation; if you find anything, please submit an [issue](https://github.com/dotstar/parameter-store/issues). However, if you want to help raise the bar, submit a [PR](https://github.com/dotstar/parameter-store/pulls)!

<!--## License

This library is licensed under the Apache 2.0 License.
-->