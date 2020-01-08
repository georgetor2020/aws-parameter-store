s3=s3://daveaws-www-us-east-1/layers/
all: layer

layer:
	mkdir -p mysql/python
	pip install -r layer-requirements.txt -t mysql/python --upgrade
	cd mysql ; zip -r ../mysql-lambda-layer.zip python
	aws s3 cp mysql-lambda-layer.zip ${s3}
