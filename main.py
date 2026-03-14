from fastapi import FastAPI, UploadFile, File
import shutil
import joblib

from ocr_utils import extract_text_from_image

app = FastAPI()

model = joblib.load("../model/model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Resume Analyzer API"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_image(file_location)

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    return {
        "predicted_job_category": prediction,
        "extracted_text_sample": text[:500]
    }