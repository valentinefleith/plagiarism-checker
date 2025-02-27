from fastapi import FastAPI
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from backend.models import TextPost

app = FastAPI()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForSequenceClassification.from_pretrained(
    "model/bert_phrases_classifier"
).to(device)
tokenizer = BertTokenizer.from_pretrained("model/bert_phrases_classifier")
label_encoder = torch.load(
    "model/label_encoder.pth", map_location=device, weights_only=False
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
    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    return {"prediction": label_encoder.inverse_transform([predicted_class])[0]}
