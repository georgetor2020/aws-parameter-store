#!/bin/bash

# Get the lambda name from cloudformation export
lambda=$(aws cloudformation list-exports --query 'Exports[][Name,Value]' --output text | grep DBLambda | cut -f 2)

echo Calling your lambda function $lambda

# Invoke Lambda with output to temporay file, then display the file.
outputfile=/tmp/out_$$.json
aws lambda invoke --function-name $lambda ${outputfile} ; cat ${outputfile}; echo ; rm ${outputfile}
