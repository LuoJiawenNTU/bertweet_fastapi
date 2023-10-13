from transformers import pipeline

def sentiment_bertweet(input_text: str):
    """
    Sentiment analysis on one sentence (str) using pre-trained model BERTweet
    """
    pipeline_bertweet = pipeline('sentiment-analysis',
                                 model='finiteautomata/bertweet-base-sentiment-analysis')
    output_list = pipeline_bertweet(input_text)
    if output_list[0]['label'] == 'POS':
        output_label = 'Positive'
    elif output_list[0]['label'] == 'NEU':
        output_label = 'Neutral'
    else:  # output_list[0]['label'] == 'NEG'
        output_label = 'Negative'

    return output_label, output_list[0]['score']
