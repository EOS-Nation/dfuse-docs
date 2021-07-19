# CODE:BEGIN:quickstarts_python_eos_section1
try:
    # python3
    from http.client import HTTPSConnection
except ImportError:
    # python2
    from httplib import HTTPSConnection

import grpc
import json
import os
import ssl
import sys

from graphql import graphql_pb2_grpc
from graphql.graphql_pb2 import Request
# CODE:END:quickstarts_python_eos_section1

# CODE:BEGIN:quickstarts_python_eos_section2
def get_token(api_key):
    connection = HTTPSConnection("auth.eosnation.io")
    connection.request('POST', '/v1/auth/issue', json.dumps({"api_key": api_key}), {'Content-type': 'application/json'})
    response = connection.getresponse()

    if response.status != 200:
        raise Exception(" Status: %s reason: %s" % (response.status, response.reason))

    token = json.loads(response.read().decode())['token']
    connection.close()

    return token
# CODE:END:quickstarts_python_eos_section2
# CODE:BEGIN:quickstarts_python_eos_section3
def create_client(endpoint):
    dfuse_api_key = os.environ.get("DFUSE_API_KEY")
    if dfuse_api_key == None:
        raise Exception("you must specify a DFUSE_API_KEY environment variable")

    channel = grpc.secure_channel(endpoint,
        credentials = grpc.composite_channel_credentials(
            grpc.ssl_channel_credentials(),
            grpc.access_token_call_credentials(get_token(dfuse_api_key))
    ))

    return graphql_pb2_grpc.GraphQLStub(channel)
# CODE:END:quickstarts_python_eos_section3
