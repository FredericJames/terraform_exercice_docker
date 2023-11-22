from fastapi import FastAPI
from connect_database import connect_with_connector_auto_iam_authn
from query_db import insertData, readData

app = FastAPI()

@app.get("/")
async def root():
    engine = connect_with_connector_auto_iam_authn()
    # insertData(engine)
    roles = readData(engine)


    return {"message": "Hello World", "roles": str(roles)}


