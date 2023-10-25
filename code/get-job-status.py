# # -*- coding: utf-8 -*-
# """
# Created on Tue Oct 25 13:05:48 2023

# @author: Subhamay Bhattacharyya
# """

import json
import logging
import boto3
import os


# # Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        logger.info(f"event : {json.dumps(event)}")

    # An error occurred
    except ParamValidationError as e:
        logger.error(f"Parameter validation error: {e}")
        return dict(
            statusCode=401, message=f"Parameter validation error: {e}")
    except ClientError as e:
        logger.error(f"Client error: {e}")
        return dict(
            statusCode=402, message=f"Parameter validation error: {e}")