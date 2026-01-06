from textblob import TextBlob

def text_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "Positive", polarity
    elif polarity < -0.3:
        return "Stressed", polarity
    else:
        return "Neutral", polarity
