from fastapi import FastAPI
from connect_database import connect_with_connector_auto_iam_authn
from query_db import insertData, readData
from predict_model import predict_custom_trained_model_sample
from requests.models import Response

app = FastAPI()

@app.get("/")
async def root():
    engine = connect_with_connector_auto_iam_authn()
    # insertData(engine)
    # roles = readData(engine)
    pred, predict_uri = predict_custom_trained_model_sample(
        project="807505896076",
        payload={"instances": [{"prompt": "Write a poem about valencia.", "max_length": 200, "top_k": 10}]},
        endpoint_id="cng-llama2",
        location="us-east1",
    )
    
    return {"message": "Hello World", "predict_uri": predict_uri, "status_code": pred.status_code, "reason": pred.reason, "json": pred.json}

