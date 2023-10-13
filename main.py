"""
API to use pre-trained model BERTweet to analyse the sentence sentiment
"""
from fastapi import FastAPI
from pydantic import BaseModel
from util_get_sentiment import sentiment_bertweet

app = FastAPI()

class InputSentence(BaseModel):
    """
    One sentence (str) text input
    """
    sentence: str

@app.get("/")
def root():
    """
    Main page
    """
    return {"message": "Hello Sentiment"}

@app.post("/sentiment")
def sentiment(input_text: InputSentence):
    """
    Generate the sentiment prediction with pre-trained model BERTweet
    """
    input_sentence = input_text.sentence
    output_label, output_score = sentiment_bertweet(input_sentence)

    return {"label": output_label,
            "score": output_score}
