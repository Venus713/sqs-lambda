"""
Simple example for Lambda->SQS->Lambda.
"""
import json
import os
import boto3

SQS_CLIENT = boto3.client('sqs')


def start(event, context):
    """
    First Lambda function. Triggered manually.
    :param event: AWS event data
    :param context: AWS function's context
    :return: ''
    """
    entry = {'data': [{'1': '3'}, {'4': '5'}]}
    for i in range(10):
        print(SQS_CLIENT.send_message(
            QueueUrl=os.getenv('SQS_URL'),
            MessageBody=json.dumps(entry),
            MessageGroupId='messageGroup1'
        ))
    return ''


def end(event, context):
    """
    Second Lambda function. Triggered by the SQS.
    :param event: AWS event data (this time will be the SQS's data)
    :param context: AWS function's context
    :return: ''
    """
    print(f'sqs event: {event}')
    body = json.loads(event['Records'][0]['body'])
    print(f"sqs parsed body: {body['data']}")
    return ''
