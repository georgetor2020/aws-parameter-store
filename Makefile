stack=ps
template=parameter-store.yml
test:
	cfn-lint ${template}

create:
	aws cloudformation create-stack --stack-name ${stack} --template-body file://${template}

update:
	aws cloudformation update-stack --stack-name ${stack} --template-body file://${template}
	
delete:
	aws cloudformation delete-stack --stack-name ${stack}