"""
Using pre-trained model BERTweet to analyse the sentence sentiment
"""
import argparse
from util_get_sentiment import sentiment_bertweet

parser = argparse.ArgumentParser()
parser.add_argument('--sentence', type=str, required=True)
args = parser.parse_args()

if __name__ == "__main__":
    print(f"Sentence for sentiment analysis: {args.sentence}")
    output_label, output_score = sentiment_bertweet(args.sentence)
    print(f"Sentiment label: {output_label}; score: {output_score}")
