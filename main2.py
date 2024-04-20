from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def sentiment():
    tokenizer = AutoTokenizer.from_pretrained("KBLab/megatron-bert-large-swedish-cased-165k")
    model = AutoModelForSequenceClassification.from_pretrained("KBLab/robust-swedish-sentiment-multiclass")

    print("start classifier...")
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    results = classifier(["Jag älskar denna produkt", "Jag hatar denna produkt", "Jag är lite tveksam till denna produkt", "Jag är reserverad till denna produkt"])

    for result in results:
        print(f"Sentence: {result['label']} with a score of {result['score']:.4f}")







if __name__ == '__main__':
    sentiment()