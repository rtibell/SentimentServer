from flask import Flask, jsonify, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

class SentimentRequest():
    workload: str

class SentimentResponse():
    label: str
    score: float

    def __init__(self, label, score):
        self.label = label
        self.score = score

    def serialize(self):
        return {"label": self.label,
                "score": self.score}
print("Load tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("KBLab/megatron-bert-large-swedish-cased-165k") #, cash_dir="./cache", force_download=True)
print("Load model...")
model = AutoModelForSequenceClassification.from_pretrained("KBLab/robust-swedish-sentiment-multiclass")

print("start classifier...")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

print("start REST-server")
app = Flask(__name__)

#@app.post('/sentiment') #, response_model=list[SentimentResponse], status_code=201)
#async def compute_sentiment(req: SentimentRequest) -> list[SentimentResponse]:
@app.route('/sentiment', methods=['POST'])
def compute_sentiment():
    request_data = request.get_json()
    results = classifier(list(request_data['workload']))
    result = results[0]
    ret_val = SentimentResponse(result['label'], result['score'])
    print("ret_val", ret_val)
    return jsonify(ret_val.serialize()), 200

if __name__ == '__main__':
    app.run(debug=True, port=8090)
