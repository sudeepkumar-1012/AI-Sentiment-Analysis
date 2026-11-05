"""
Text Preprocessing Module
Handles text cleaning, tokenization, and stopword removal
"""

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def ensure_nltk_data():
    """Ensure required NLTK resources are installed."""
    resources = {
        'punkt': 'tokenizers/punkt',
        'stopwords': 'corpora/stopwords'
    }
    for package, resource_path in resources.items():
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(package)


ensure_nltk_data()


class TextPreprocessor:
    """
    Preprocesses text for sentiment analysis and NLP tasks
    """

    def __init__(self):
        """Initialize preprocessor with stopwords."""
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """
        Clean text: lowercase, remove URLs, special characters, extra whitespace.

        Args:
            text (str): Raw text to clean.

        Returns:
            str: Cleaned text.
        """
        if not isinstance(text, str):
            return ''

        text = text.lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = ' '.join(text.split())

        return text

    def remove_stopwords(self, text):
        """
        Remove common stopwords from text.

        Args:
            text (str): Text to process.

        Returns:
            str: Text without stopwords.
        """
        words = text.split()
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def tokenize(self, text):
        """
        Tokenize text into words.

        Args:
            text (str): Text to tokenize.

        Returns:
            list: List of tokens.
        """
        return word_tokenize(text)

    def preprocess(self, text, remove_stopwords=False):
        """
        Complete preprocessing pipeline.

        Args:
            text (str): Raw text.
            remove_stopwords (bool): Remove stopwords when True.

        Returns:
            str: Preprocessed text.
        """
        cleaned = self.clean_text(text)
        if remove_stopwords:
            cleaned = self.remove_stopwords(cleaned)
        return cleaned

    def preprocess_batch(self, texts, remove_stopwords=False):
        """
        Preprocess multiple text entries.

        Args:
            texts (list): List of text strings.
            remove_stopwords (bool): Remove stopwords when True.

        Returns:
            list: List of preprocessed text strings.
        """
        return [self.preprocess(text, remove_stopwords) for text in texts]
