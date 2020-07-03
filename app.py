#!flask/bin/python
from flask import Flask, jsonify
import boto3

client = boto3.client('pricing', region_name='us-east-1')

app = Flask(__name__)

@app.route('/todo/api/v1.0/pricing', methods=['GET'])
def get_pricing():
    response = client.get_products(
        ServiceCode='AmazonRDS',
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
        ],
        FormatVersion='aws_v1'
    )
    return jsonify({'pricing': response})

if __name__ == '__main__':
    app.run(debug=True)