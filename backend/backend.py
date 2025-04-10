import numpy as np
import json
import pandas as pd
from pathlib import Path
from tqdm import tqdm
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from typing import Optional, List

import sys
sys.path.append("machine-translation-transformer/src")
from utils.translator import translate as translatex
from model_initialization import model_initialize_en_to_vn, model_initialize_vn_to_en


class Item(BaseModel):
    lang: Optional[str] = None
    prompt: Optional[str] = None

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/api/translate")
def translate(inputData: Item):

    translated_output = ""

    if inputData.lang == "en_to_vn":
        translated_output = translatex(inputData.prompt, model_en_to_vn, src_field_en_to_vn, trg_field_en_to_vn, max_strlen, device, k)
    else:
        translated_output = translatex(inputData.prompt, model_vn_to_en, src_field_vn_to_en, trg_field_vn_to_en, max_strlen, device, k)

    return {
        "response": translated_output
    }

if __name__ == '__main__':
    try:
        model_en_to_vn, src_field_en_to_vn, trg_field_en_to_vn, max_strlen, device, k = model_initialize_en_to_vn()
        model_vn_to_en, src_field_vn_to_en, trg_field_vn_to_en, max_strlen, device, k = model_initialize_vn_to_en()
        print("successfully initialize two models")
    except Exception as e:
        print(e)
        raise(e)
    
    try:
        uvicorn.run(app, host="0.0.0.0", port=8053)
        print("successfully initialize the fastapi application")
    except Exception as e:
        print("Errors with the fastapi app initialization: ", e)