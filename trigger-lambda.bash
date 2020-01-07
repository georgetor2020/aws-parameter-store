#!/bin/bash

# Get the lambda name from cloudformation export

lambda=$(aws cloudformation list-exports --query 'Exports[][Name,Value]' --output text | grep DBLambda | cut -f 2)

echo Calling your lambda function $lambda

outputfile=/tmp/out_$$.json
aws lambda invoke --function-name ps-p2 ${outputfile} ; cat ${outputfile}; echo ; rm ${outputfile}