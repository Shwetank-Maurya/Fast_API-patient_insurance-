from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from schema.prediction_response import PredictionResponse
from schema.user_input import UserInput
from model.predict import MODEL_VERSION,model,predict_output

app = FastAPI()

@app.get('/')
def home():
    return{'message':'Insurance Premimum Prediction App'}

@app.get('/health')
def health_check():
    return{
        'status':'OK',
        'version':MODEL_VERSION,
        'model_loaded':model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input= {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    prediction = predict_output(user_input)

    return JSONResponse(status_code=200, content={'predicted_category': prediction})




