import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    my_variable = os.environ['VARIABLE_NAME']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "greeting": "Hello and wellcome again, the variable is {}".format(my_variable)
        }),
    }
