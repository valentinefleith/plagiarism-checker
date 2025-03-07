from fastapi import FastAPI
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from torch.nn.functional import softmax
from backend.models import TextPost
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
       "http://localhost:8080",   
    "http://192.168.0.38:8080", ### c'est le frontend ça 
    "http://127.0.0.1:8000",    # et ça le back
]

## autorisation d'accès pour les requetes api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

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
    probas = softmax(outputs.logits, dim=1).cpu().detach().numpy()
    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    predicted_classname = label_encoder.inverse_transform([predicted_class])[0]
    proba = (
        probas[0].tolist()[0]
        if predicted_classname == "human"
        else probas[0].tolist()[1]
    )
    return {"prediction": predicted_classname, "probability": round(proba * 100, 1)}
