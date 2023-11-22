from typing import Dict, List, Union

from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

import requests as r
from requests.models import Response


def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    payload: str,
    location: str = "us-east1",
    api_endpoint: str = "us-east1-aiplatform.googleapis.com",
) -> Response:
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    
    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    endpoint_client = aiplatform.gapic.EndpointServiceClient(client_options=client_options)
    endpoint_dict = endpoint_client.get_endpoint(name=endpoint)
    predict_uri = endpoint_dict.deployed_models[0].private_endpoints.predict_http_uri

    res = r.post(predict_uri, json=payload)
    return res, predict_uri
    
