# BERTweet_FastAPI
This is a simple example/tutorial for using the pre-trained NLP model (BERTweet) available on Huggingface (Python package: *transformer*) and FastAPI
# Main Files
## util_get_sentiment.py
Function: sentiment_bertweet  
Input: a sentence (str)  
Output: sentiment label ('Positive', 'Neutral', 'Negative') and score predicted by BERTweet model
## try_tranformer_bertweet.ipynb
Step-by-step demonstration of how to get the pre-trained model from Huggingface and do the prediction  
Also demonstrating how to use sentiment_bertweet in util_get_sentiment.py  
BERTweet ability with Python package *emoji*