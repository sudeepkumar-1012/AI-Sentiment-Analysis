# Smart Review Analyzer & Product Recommendation System

A complete end-to-end Python web application for analyzing customer reviews using AI-powered sentiment analysis and generating product recommendations.

## Features ✨

- **Easy Review Upload**: Upload CSV files or enter reviews manually
- **AI Sentiment Analysis**: VADER sentiment analyzer with optional RoBERTa support
- **Text Preprocessing**: Automatic cleaning, tokenization, and stopword removal using NLTK
- **Visual Analytics**: Beautiful charts and graphs for sentiment distribution
- **Smart Recommendations**: AI-powered product recommendations based on sentiment scores
- **REST API**: Built-in API endpoint (`/analyze`) for programmatic access
- **Responsive UI**: Clean, modern web interface with Bootstrap
- **Product Analysis**: Analyze sentiment by product with recommendations

## Tech Stack 🛠️

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap 5
- **NLP**: NLTK, VADER sentiment analyzer
- **Advanced NLP** (Optional): Hugging Face Transformers (RoBERTa)
- **Visualization**: Matplotlib
- **Data Handling**: Pandas
- **Python Version**: 3.10+

## Project Structure 📁

```
smart-review-analyzer/
├── app.py                      # Main Flask application
├── visualizations.py           # Chart and graph generation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navbar
│   ├── index.html             # Home page
│   ├── results.html           # Results page
│   └── error.html             # Error page
│
├── static/                    # Static files
│   ├── css/
│   │   └── style.css          # Custom CSS styles
│   └── js/
│       └── script.js          # Client-side JavaScript
│
├── utils/                     # Utility modules
│   ├── preprocessing.py       # Text preprocessing
│   ├── sentiment_analyzer.py  # Sentiment analysis
│   └── recommendation_engine.py # Product recommendations
│
└── data/                      # Sample data
    └── sample_reviews.csv     # Sample review data
```

## Installation 🚀

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Download the Project
```bash
cd smart-review-analyzer
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download NLTK Data (One-time)
The application automatically downloads required NLTK data on first run, but you can pre-download it:

```bash
python -c "
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
"
```

### Step 5 (Optional): Install Transformers for RoBERTa
For advanced RoBERTa sentiment analysis:
```bash
pip install transformers torch
```

## Running the Application ▶️

### Start the Flask Server
```bash
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage Guide 📖

### 1. Upload CSV File
- Click on the **"Upload CSV"** tab
- Select a CSV file with review data
- CSV should contain:
  - Required: `review` or `text` column (review content)
  - Optional: `product` column (for product-specific analysis)
- Click **"Analyze Reviews"**

### 2. Manual Input
- Click on the **"Manual Input"** tab
- Enter reviews separated by new lines (one review per line)
- Click **"Analyze Reviews"**

### 3. View Results
- Sentiment distribution (Positive, Negative, Neutral %)
- Individual review sentiment scores
- Visual charts and graphs
- Top recommended products (if product column exists)
- Download results as JSON

## API Endpoints 🔌

### `/analyze` (POST)
Analyze reviews and return sentiment results.

**Request:**
```bash
curl -X POST http://localhost:5000/analyze \
  -F "file=@sample_reviews.csv" \
  -F "use_roberta=false"
```

**Response:**
```json
{
  "success": true,
  "summary": {
    "total": 20,
    "positive_count": 10,
    "negative_count": 5,
    "neutral_count": 5,
    "positive_percentage": 50.0,
    "negative_percentage": 25.0,
    "neutral_percentage": 25.0,
    "average_compound": 0.245
  },
  "reviews": [...],
  "recommendations": {...},
  "charts": {...},
  "total_reviews": 20
}
```

### `/api/sample-data` (GET)
Download sample CSV file.

```bash
curl http://localhost:5000/api/sample-data -o sample.csv
```

### `/api/health` (GET)
Health check endpoint.

```bash
curl http://localhost:5000/api/health
```

## CSV File Format 📋

### Example CSV Structure
```csv
product,review
Laptop A,Amazing laptop! Very fast and reliable.
Laptop A,Good performance but battery life could be better.
Headphones B,Very comfortable and sound quality is superb.
```

### Required Columns
- `review` or `text`: The review content (required)

### Optional Columns
- `product`: Product name (enables product recommendations)
- Other columns are ignored

## Sentiment Analysis Details 🧠

### VADER Sentiment Analyzer
- **Advantages**: Fast, rule-based, works well on social media text
- **Output**: 
  - Positive score (0-1)
  - Negative score (0-1)
  - Neutral score (0-1)
  - Compound score (-1 to 1): Overall sentiment
- **Labels**:
  - Positive: compound ≥ 0.05
  - Negative: compound ≤ -0.05
  - Neutral: -0.05 < compound < 0.05

### RoBERTa Sentiment Analyzer (Optional)
- **Advantages**: Deep learning based, more accurate for complex sentences
- **Requires**: `transformers` and `torch` libraries
- **Note**: Slower than VADER but more accurate
- Enable by checking "Use RoBERTa" option

## Text Preprocessing 🔤

The application performs these preprocessing steps:

1. **Lowercase**: Convert text to lowercase
2. **URL Removal**: Remove URLs from text
3. **Email Removal**: Remove email addresses
4. **Special Character Removal**: Keep only letters and spaces
5. **Whitespace Normalization**: Remove extra spaces
6. **Tokenization**: Split text into words (optional)
7. **Stopword Removal**: Remove common words like "the", "a", etc. (optional)

## Product Recommendations 🎯

The recommendation engine:
- Calculates average sentiment score for each product
- Filters products with positive sentiment (score ≥ 0.05)
- Sorts by highest sentiment score
- Returns top N products (default: 5)

Example recommendation output:
```json
{
  "recommendations": [
    {
      "product": "Laptop A",
      "average_score": 0.45,
      "positive_percentage": 75.0,
      "total_reviews": 4
    }
  ]
}
```

## Visualization 📊

The application generates:

1. **Sentiment Distribution Pie Chart**
   - Shows percentage breakdown of positive, negative, neutral
   - Color-coded for easy interpretation

2. **Product Sentiment Bar Chart** (if product column exists)
   - Average sentiment score by product
   - Helps identify top-rated and poorly-rated products

## Troubleshooting 🔧

### Issue: Module not found errors
**Solution**: Make sure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### Issue: NLTK data not found
**Solution**: Download NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

### Issue: Port 5000 already in use
**Solution**: Either stop the other application or modify the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change port to 5001
```

### Issue: RoBERTa model too large/slow
**Solution**: Disable RoBERTa and use VADER only (default behavior). RoBERTa is optional.

## Code Examples 💻

### Using the preprocessing module
```python
from utils.preprocessing import TextPreprocessor

preprocessor = TextPreprocessor()
text = "Amazing product! Very satisfied with my purchase."
cleaned = preprocessor.preprocess(text)
print(cleaned)  # Output: "amazing product satisfied purchase"
```

### Using sentiment analyzer
```python
from utils.sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()
review = "This product is excellent!"
result = analyzer.analyze_text(review)
print(result)
# Output: {'text': 'This product is excellent!', 'vader': {...}}
```

### Using recommendation engine
```python
from utils.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()
reviews = [...]  # List of reviews with sentiment
recommendations = engine.get_recommendations(reviews, top_n=5)
print(recommendations)
```

## Advanced Features 🚀

### Custom Sentiment Thresholds
Modify sentiment labels in `utils/sentiment_analyzer.py`:
```python
# Change thresholds
if compound >= 0.1:  # More strict for positive
    label = 'positive'
```

### Batch Processing
Process large CSV files in chunks for better performance:
```python
# In app.py, modify the /analyze endpoint to process in chunks
CHUNK_SIZE = 1000
```

### Custom Visualization
Add more chart types in `visualizations.py`:
```python
def create_custom_chart(data):
    # Create your own chart
    pass
```

## Performance Tips ⚡

1. **Use VADER by default** (faster than RoBERTa)
2. **Batch process large files** (1000+ reviews)
3. **Cache NLTK data** (pre-download on startup)
4. **Use appropriate preprocessing** (don't over-process)
5. **Monitor memory usage** (large CSV files)

## Dependencies 📚

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3 | Web framework |
| pandas | 2.0.3 | Data handling |
| nltk | 3.8.1 | NLP toolkit |
| matplotlib | 3.7.2 | Visualization |
| Pillow | 10.0.0 | Image handling |
| transformers | 4.32.0 | RoBERTa (optional) |
| torch | 2.0.1 | PyTorch (optional) |

## Security Considerations 🔒

- Input validation on file uploads
- File size limits (16MB)
- XSS protection via template escaping
- CSRF protection (can be added)
- SQL injection protection (N/A - no database)

## Contributing 🤝

To contribute improvements:
1. Fork the project
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License 📄

This project is open source and available under the MIT License.

## Support 💬

For issues, questions, or suggestions:
- Check the troubleshooting section
- Review the code comments
- Examine the sample CSV file

## Roadmap 🗺️

Potential future enhancements:
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication
- [ ] Review scheduling and automation
- [ ] Advanced visualization (D3.js)
- [ ] Export to PDF
- [ ] Mobile app
- [ ] Real-time analysis dashboard
- [ ] Multi-language support
- [ ] Custom ML models
- [ ] API rate limiting

## Credits 🙏

Built with:
- Flask documentation
- NLTK documentation
- Hugging Face transformers
- Bootstrap framework
- Chart.js for visualizations

## Version History 📝

### v1.0.0 (Initial Release)
- Core sentiment analysis
- VADER analyzer
- Basic web interface
- CSV upload
- Recommendation system
- Visualization support

---

**Enjoy analyzing reviews! 🎉**

For more information, visit the [Flask documentation](https://flask.palletsprojects.com/) and [NLTK documentation](https://www.nltk.org/).
