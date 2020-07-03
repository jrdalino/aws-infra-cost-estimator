#!flask/bin/python
from flask import Flask, jsonify
import boto3

client = boto3.client('pricing', region_name='us-east-1')

app = Flask(__name__)

@app.route('/api/v1.0/services', methods=['GET'])
def describe_services():
    response = client.describe_services(
        ServiceCode='AmazonEC2',        
        FormatVersion='aws_v1',
        MaxResults=3
    )
    return jsonify({'services': response})

@app.route('/api/v1.0/products', methods=['GET'])
def get_products():
    response = client.get_products(
        ServiceCode='AmazonRDS',
        FormatVersion='aws_v1',
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'instanceType',
                'Value': 'db.m3.large'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'databaseEngine',
                'Value': 'mysql'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'deploymentOption',
                'Value': 'Multi-AZ'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': 'Asia Pacific (Singapore)'
            },
        ]
    )
    return jsonify({'products': response})

if __name__ == '__main__':
    app.run(debug=True)