import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("#### I am logging Lambda versioning")

    request_body = json.loads(event.get('body'))

    name = request_body.get('name')

    if name == 'Joker':
        raise ValueError('Bad guys should not be greeted')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "greeting": "Hello and wellcome again " + name,
        }),
    }
