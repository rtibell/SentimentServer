from transformers import pipeline
import tensorflow as tf

def sentiment():
    # Initialize a sentiment analysis pipeline
    classifier = pipeline('sentiment-analysis', model='xlm-roberta-base')

    # Example text in Swedish
    print("start classifier...")
    results = classifier(["Jag älskar denna produkt", "Jag hatar denna produkt"])
    for result in results:
        print(f"Sentence: {result['label']} with a score of {result['score']:.4f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentiment()
