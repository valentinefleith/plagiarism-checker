import os
from fastapi import FastAPI
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from torch.nn.functional import softmax
from .models import TextPost
from fastapi.middleware.cors import CORSMiddleware

MODEL_PATH = os.getenv("MODEL_PATH", "backend/model")

app = FastAPI()

## autorisation d'accès pour les requetes api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForSequenceClassification.from_pretrained(
    f"{MODEL_PATH}/bert_phrases_classifier"
).to(device)
tokenizer = BertTokenizer.from_pretrained(f"{MODEL_PATH}/bert_phrases_classifier")
label_encoder = torch.load(
    f"{MODEL_PATH}/label_encoder.pth", map_location=device, weights_only=False
)


@app.get("/")
def root():
    return {"message": "Hello app!"}


@app.post("/prediction/")
async def predict_class(text: TextPost):
    inputs = tokenizer(
        text.body,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=128,
    ).to(device)

    outputs = model(**inputs)
    probas = softmax(outputs.logits, dim=1).cpu().detach().numpy()
    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    predicted_classname = label_encoder.inverse_transform([predicted_class])[0]
    proba = probas[0].tolist()[1]
    return {
        "text": text.body,
        "prediction": predicted_classname,
        "probability": round(proba * 100, 1),
    }
