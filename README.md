# AWS Infra Cost Estimator

## Setup
- Activate virtual environment before installing flask, flask-cors and boto3
```
$ cd ~/environment/aws-infra-cost-estimator
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ venv/bin/pip install flask flask-cors boto3
(venv) $ deactivate # To deactivate
```

## Run Locally
```
$ python app.py
$ curl http://localhost:5000
```



https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html