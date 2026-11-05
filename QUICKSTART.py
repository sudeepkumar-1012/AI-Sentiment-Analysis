"""
Quick Start Guide - Smart Review Analyzer
"""

# ============================================
# INSTALLATION & SETUP
# ============================================

# 1. Create virtual environment
# python -m venv venv

# 2. Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# 3. Install dependencies
# pip install -r requirements.txt

# 4. Download NLTK data (one-time)
# python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"

# ============================================
# RUN THE APPLICATION
# ============================================

# python app.py

# Then open browser: http://localhost:5000

# ============================================
# USING THE APPLICATION
# ============================================

# 1. HOME PAGE
#    - Upload CSV file with 'review' and optional 'product' columns
#    - Or manually enter reviews
#    - Click "Analyze Reviews"

# 2. RESULTS PAGE
#    - View sentiment distribution (pie chart)
#    - See product recommendations
#    - Review individual sentiment scores
#    - Filter by sentiment (positive, negative, neutral)
#    - Download results as JSON

# ============================================
# CSV FILE FORMAT
# ============================================

# Required columns:
#   - review (or text): The review content
#
# Optional columns:
#   - product: Product name
#
# Example:
#   product,review
#   Laptop A,Amazing laptop! Very fast.
#   Laptop A,Great build quality.
#   Phone B,Not satisfied with battery.

# ============================================
# API ENDPOINTS
# ============================================

# POST /analyze
#   Upload reviews and get sentiment analysis
#   Request: CSV file or manual text
#   Response: JSON with sentiment scores, charts, recommendations
#
# GET /api/sample-data
#   Download sample CSV file
#
# GET /api/health
#   Health check endpoint

# ============================================
# PROJECT STRUCTURE
# ============================================

# app.py                    - Main Flask application
# visualizations.py         - Chart generation
# requirements.txt          - Dependencies
# README.md                 - Full documentation
#
# templates/
#   base.html               - Base template
#   index.html              - Home page
#   results.html            - Results page
#   error.html              - Error page
#
# static/
#   css/style.css           - Styling
#   js/script.js            - Client-side JS
#
# utils/
#   preprocessing.py        - Text preprocessing
#   sentiment_analyzer.py   - VADER & RoBERTa
#   recommendation_engine.py - Product recommendations
#
# data/
#   sample_reviews.csv      - Sample data

# ============================================
# SENTIMENT ANALYSIS EXPLAINED
# ============================================

# VADER Scores:
#   - pos (0-1): Positive sentiment proportion
#   - neg (0-1): Negative sentiment proportion
#   - neu (0-1): Neutral sentiment proportion
#   - compound (-1 to 1): Overall sentiment score
#
# Interpretation:
#   - compound >= 0.05: Positive
#   - compound <= -0.05: Negative
#   - -0.05 < compound < 0.05: Neutral
#
# Example:
#   Review: "Great product! Very satisfied!"
#   VADER Score:
#     pos: 0.756
#     neg: 0.000
#     neu: 0.244
#     compound: 0.816
#   Label: Positive

# ============================================
# TROUBLESHOOTING
# ============================================

# Issue: Module not found
# Solution: pip install -r requirements.txt

# Issue: NLTK data not found
# Solution: python -c "import nltk; nltk.download('punkt')"

# Issue: Port 5000 in use
# Solution: Change port in app.py or stop other service

# Issue: RoBERTa too slow
# Solution: Keep "Use RoBERTa" unchecked (use VADER only)

# ============================================
# CODE EXAMPLES
# ============================================

# Example 1: Preprocess text
# from utils.preprocessing import TextPreprocessor
# preprocessor = TextPreprocessor()
# result = preprocessor.preprocess("Great product!!!")
# print(result)  # "great product"

# Example 2: Analyze sentiment
# from utils.sentiment_analyzer import SentimentAnalyzer
# analyzer = SentimentAnalyzer()
# sentiment = analyzer.analyze_text("This is amazing!")
# print(sentiment['vader']['label'])  # positive

# Example 3: Get recommendations
# from utils.recommendation_engine import RecommendationEngine
# engine = RecommendationEngine()
# recs = engine.get_recommendations(reviews_data, top_n=5)
# print(recs['recommendations'])

# ============================================
# KEYBOARD SHORTCUTS
# ============================================

# Ctrl+L: Focus address bar (go to http://localhost:5000)
# F12: Open developer console
# Ctrl+Shift+C: Inspect element

# ============================================
# USEFUL COMMANDS
# ============================================

# Check Flask version: pip show Flask
# List all packages: pip list
# Freeze requirements: pip freeze > requirements.txt
# Update pip: pip install --upgrade pip
# Deactivate venv: deactivate

# ============================================
# NEXT STEPS
# ============================================

# 1. Download sample_reviews.csv from the app
# 2. Upload and analyze the sample reviews
# 3. Try manual text input
# 4. Check the visualization and recommendations
# 5. Download results
# 6. Explore the API endpoints
# 7. Read full README.md for advanced features

print("""
╔════════════════════════════════════════════════════════════════════╗
║   Smart Review Analyzer & Product Recommendation System           ║
║                       Quick Start Guide                           ║
╚════════════════════════════════════════════════════════════════════╝

1. INSTALLATION:
   python -m venv venv
   venv\\Scripts\\activate (Windows) or source venv/bin/activate (Mac/Linux)
   pip install -r requirements.txt

2. RUN:
   python app.py
   Open: http://localhost:5000

3. ANALYZE:
   - Upload CSV with 'review' column
   - Or enter reviews manually
   - Click "Analyze Reviews"

4. VIEW RESULTS:
   - Sentiment distribution (%)
   - Product recommendations
   - Individual review scores
   - Download as JSON

5. FEATURES:
   ✓ VADER sentiment analysis
   ✓ Text preprocessing with NLTK
   ✓ Beautiful visualization
   ✓ Smart recommendations
   ✓ REST API endpoint
   ✓ Responsive web UI

For more info, see README.md
""")
