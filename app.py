"""
Flask Sentiment Analysis App

Setup Instructions:
1. python -m venv venv
2. venv\Scripts\activate
3. python -m pip install --upgrade pip setuptools wheel
4. pip install -r requirements.txt
5. python app.py
6. If NLTK data is missing, run:
   python -m nltk.downloader punkt stopwords vader_lexicon
"""

import os

import pandas as pd
from flask import Flask, render_template, request

from utils.preprocessing import TextPreprocessor
from utils.recommendation_engine import RecommendationEngine
from utils.sentiment_analyzer import SentimentAnalyzer
from visualizations import create_sentiment_chart, create_product_chart

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize utilities
preprocessor = TextPreprocessor()
sentiment_analyzer = SentimentAnalyzer()
recommendation_engine = RecommendationEngine()


def extract_reviews_and_products(df):
    """Extract review text and optional product names from a CSV DataFrame."""
    if 'review' in df.columns:
        reviews = df['review'].astype(str).tolist()
    elif 'text' in df.columns:
        reviews = df['text'].astype(str).tolist()
    elif len(df.columns) > 0:
        reviews = df.iloc[:, 0].astype(str).tolist()
    else:
        raise ValueError('CSV file must contain at least one text column.')

    product_column = None
    if 'product' in df.columns:
        product_column = df['product'].astype(str).tolist()
    elif 'product_name' in df.columns:
        product_column = df['product_name'].astype(str).tolist()

    return reviews, product_column


@app.route('/', methods=['GET'])
def home():
    """Render the main home page."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Process form input, analyze sentiment, and render results."""
    try:
        reviews = []
        product_column = None

        csv_file = request.files.get('file')
        manual_text = request.form.get('manual_text', '').strip()
        use_roberta = request.form.get('use_roberta') == 'on'

        if csv_file and csv_file.filename:
            try:
                df = pd.read_csv(csv_file)
            except Exception as exc:
                raise ValueError(f'Unable to read CSV file: {exc}')

            reviews, product_column = extract_reviews_and_products(df)

        elif manual_text:
            reviews = [line.strip() for line in manual_text.splitlines() if line.strip()]
        else:
            raise ValueError('Please upload a CSV file or enter at least one review manually.')

        if not reviews:
            raise ValueError('No reviews found to analyze. Please provide valid text.')

        # Preprocess and analyze reviews
        cleaned_reviews = preprocessor.preprocess_batch(reviews)
        sentiment_results = sentiment_analyzer.analyze_batch(cleaned_reviews, use_roberta)

        reviews_data = []
        for index, (original, cleaned, sentiment) in enumerate(zip(reviews, cleaned_reviews, sentiment_results), start=1):
            review_data = {
                'index': index,
                'original_text': original,
                'preprocessed_text': cleaned,
                'sentiment': sentiment['vader'],
                'label': sentiment['vader']['label']
            }
            if product_column:
                review_data['product'] = product_column[index - 1]
            if sentiment.get('roberta'):
                review_data['roberta'] = sentiment['roberta']
            reviews_data.append(review_data)

        sentiment_summary = sentiment_analyzer.get_sentiment_summary(cleaned_reviews, use_roberta)
        sentiment_chart = create_sentiment_chart(sentiment_summary)
        product_chart = create_product_chart(reviews_data) if product_column else None

        recommendations = recommendation_engine.get_recommendations(reviews_data) if product_column else None

        return render_template(
            'results.html',
            reviews=reviews_data,
            summary=sentiment_summary,
            sentiment_chart=sentiment_chart,
            product_chart=product_chart,
            recommendations=recommendations,
            total_reviews=len(reviews_data),
            use_roberta=use_roberta
        )

    except LookupError:
        return render_template(
            'error.html',
            error='Missing NLTK data. Run: python -m nltk.downloader punkt stopwords vader_lexicon'
        )
    except ValueError as exc:
        return render_template('error.html', error=str(exc))
    except Exception as exc:
        return render_template('error.html', error=f'Unexpected error: {exc}')


@app.route('/sample-data', methods=['GET'])
def sample_data():
    """Download a sample CSV file for testing."""
    sample_data = {
        'product': ['Laptop A', 'Laptop A', 'Headphones B', 'Headphones B'],
        'review': [
            'Amazing laptop! Very fast and reliable. Great display quality.',
            'Good performance but battery life could be better.',
            'Very comfortable and sound quality is superb.',
            'Headphones broke after 2 months. Not worth it.'
        ]
    }
    df = pd.DataFrame(sample_data)
    csv_buffer = df.to_csv(index=False)
    return csv_buffer, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=sample_reviews.csv'
    }


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Page not found.'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', error='Internal server error.'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
