#
# Makefile for DB portion of Parameter Store Lab
#
stack=ps-db
template=aurora.yaml
parameters=aurora_parameters.json
test:
	cfn-lint ${template} --ignore-checks W3010,W1001

create:
	aws cloudformation create-stack \
	  --stack-name ${stack} \
	  --template-body file://${template} \
	  --parameters file://${parameters} \
  	  --capabilities CAPABILITY_NAMED_IAM

update:
	aws cloudformation update-stack \
	--stack-name ${stack} \
	--template-body file://${template} \
	--parameters file://${parameters} \
	--capabilities CAPABILITY_NAMED_IAM
	
delete:
	aws cloudformation delete-stack --stack-name ${stack}

outputs:
	aws cloudformation describe-stacks --stack-name ${stack} --query Stacks[].Outputs[] 
	
layers:
	cd lambda ; make

resources:
	aws cloudformation describe-stack-resources --stack-name ${stack} --query StackResources[].[LogicalResourceId,ResourceStatus,Timestamp] --output table
