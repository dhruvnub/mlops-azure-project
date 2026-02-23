from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Spam Detection API Running"}

@app.get("/predict")
def predict(text: str):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return {"prediction": "Spam" if prediction == 1 else "Not Spam"}