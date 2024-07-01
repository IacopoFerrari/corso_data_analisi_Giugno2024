from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
import pandas as pd



app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/")
def show_records():
    df = pd.read_csv('sars_2003_complete_dataset.csv')
    result = df.to_json(orient="records")
    return JSONResponse(content=result)    

@app.get("/records/{paese}")
def show_records_for_country(paese):
    df = pd.read_csv('sars_2003_complete_dataset.csv')
    record = df[df["country"]==paese.strip()]
    if not record.empty:
        result = record.to_json()
        return JSONResponse(content=result)    

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="paese non presente in lista")