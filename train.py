import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample tiny dataset
data = {
    "text": [
        "Win money now",
        "Limited time offer",
        "Meeting at 10am",
        "Project discussion tomorrow",
        "Claim your prize now",
        "Let's have lunch"
    ],
    "label": [1,1,0,0,1,0]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)

joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Spam model trained and saved successfully")