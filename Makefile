stack=ps
template=parameter-store.yml
parameters=parameters.json
test:
	cfn-lint ${template} --ignore-checks W3010

create:
	aws cloudformation create-stack \
	  --stack-name ${stack} \
	  --template-body file://${template}

update:
	aws cloudformation update-stack --stack-name ${stack} --template-body file://${template} --parameters file://${parameters}
	
delete:
	aws cloudformation delete-stack --stack-name ${stack}