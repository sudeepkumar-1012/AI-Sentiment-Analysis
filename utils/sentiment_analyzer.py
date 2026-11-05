"""
Sentiment Analysis Module
Performs sentiment analysis using VADER and optionally RoBERTa.
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def ensure_nltk_data():
    """Ensure VADER lexicon is installed."""
    try:
        nltk.data.find('sentiment/vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon')


ensure_nltk_data()

# Optional RoBERTa sentiment analysis support.
ROBERTA_AVAILABLE = False
try:
    from transformers import pipeline
    ROBERTA_AVAILABLE = True
except ImportError:
    pass


class SentimentAnalyzer:
    """
    Analyzes sentiment of text using VADER and optional RoBERTa.
    """

    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        self.roberta = None
        if ROBERTA_AVAILABLE:
            try:
                self.roberta = pipeline('sentiment-analysis', model='roberta-base')
            except Exception:
                self.roberta = None

    def analyze_vader(self, text):
        """Analyze sentiment with VADER."""
        if not text or not isinstance(text, str):
            return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0, 'label': 'neutral'}

        scores = self.vader.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            label = 'positive'
        elif compound <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'

        scores['label'] = label
        return scores

    def analyze_roberta(self, text):
        """Analyze sentiment with RoBERTa when available."""
        if not self.roberta:
            return None
        try:
            text = text[:512]
            result = self.roberta(text)[0]
            return {'label': result['label'].lower(), 'score': round(result['score'], 4)}
        except Exception:
            return None

    def analyze_text(self, text, use_roberta=False):
        """Analyze a single text string."""
        result = {'text': text[:100] + '...' if isinstance(text, str) and len(text) > 100 else text}
        result['vader'] = self.analyze_vader(text)
        if use_roberta and self.roberta:
            roberta_result = self.analyze_roberta(text)
            if roberta_result:
                result['roberta'] = roberta_result
        return result

    def analyze_batch(self, texts, use_roberta=False):
        """Analyze a list of texts."""
        return [self.analyze_text(text, use_roberta) for text in texts]

    def get_sentiment_summary(self, texts, use_roberta=False):
        """Return aggregate sentiment statistics for a list of texts."""
        if not texts:
            return {
                'total': 0,
                'positive_count': 0,
                'negative_count': 0,
                'neutral_count': 0,
                'positive_percentage': 0,
                'negative_percentage': 0,
                'neutral_percentage': 0,
                'average_compound': 0.0
            }

        results = self.analyze_batch(texts, use_roberta)
        positive = negative = neutral = 0
        total_compound = 0.0

        for sentiment in results:
            label = sentiment['vader']['label']
            if label == 'positive':
                positive += 1
            elif label == 'negative':
                negative += 1
            else:
                neutral += 1
            total_compound += sentiment['vader']['compound']

        total = len(results)
        return {
            'total': total,
            'positive_count': positive,
            'negative_count': negative,
            'neutral_count': neutral,
            'positive_percentage': round((positive / total) * 100, 2) if total else 0,
            'negative_percentage': round((negative / total) * 100, 2) if total else 0,
            'neutral_percentage': round((neutral / total) * 100, 2) if total else 0,
            'average_compound': round(total_compound / total, 4) if total else 0.0
        }
