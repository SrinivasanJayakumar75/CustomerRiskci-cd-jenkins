#Docker commands

docker build -t customer:v1 .
docker build -t srinivasan7500/srinivasan:latest . 
docker push srinivasan7500/srinivasan:latest

docker run -d -it --name modelv1 -p 8005:8005 srinivasan7500/srinivasan:latest bash

docker exec modelv1 python prediction_model/training_pipeline.py

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear

docker cp modelv1:/code/src/TestResults.xml .

docker exec -d -w /code modelv1 python main.py

#jenkins admin

sudo cat /var/lib/jenkins/secrets/initialAdminPassword


