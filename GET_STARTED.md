# 🚀 RUN YOUR APPLICATION - STEP BY STEP

## Starting Your Smart Review Analyzer

### WINDOWS USERS - Follow These Steps:

#### Step 1: Open Command Prompt
- Press `Win + R`
- Type `cmd`
- Press Enter

#### Step 2: Navigate to Project Folder
```
cd Desktop\sudeep\final\ faahhhh
```
(Replace with your actual path if different)

#### Step 3: Create Virtual Environment
```
python -m venv venv
```
This creates a isolated Python environment.

#### Step 4: Activate Virtual Environment
```
venv\Scripts\activate
```
You should see `(venv)` at the beginning of the command prompt.

#### Step 5: Install All Dependencies
```
pip install -r requirements.txt
```
This installs Flask, NLTK, Matplotlib, Pandas, etc. (May take 2-3 minutes)

#### Step 6: Download NLP Data
```
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```
This downloads necessary NLTK data for text processing.

#### Step 7: Run the Application
```
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

#### Step 8: Open in Browser
- Open your web browser (Chrome, Firefox, Edge, etc.)
- Go to: `http://localhost:5000`

### Success! 🎉
You should see the Smart Review Analyzer homepage!

---

## MAC/LINUX USERS - Follow These Steps:

#### Step 1: Open Terminal
- Press `Cmd + Space`
- Type `terminal`
- Press Enter
(Or open Terminal from Applications > Utilities)

#### Step 2: Navigate to Project Folder
```
cd path/to/smart-review-analyzer
```

#### Step 3: Create Virtual Environment
```
python3 -m venv venv
```

#### Step 4: Activate Virtual Environment
```
source venv/bin/activate
```
You should see `(venv)` at the beginning of the terminal.

#### Step 5: Install All Dependencies
```
pip install -r requirements.txt
```

#### Step 6: Download NLP Data
```
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

#### Step 7: Run the Application
```
python app.py
```

#### Step 8: Open in Browser
- Open your web browser
- Go to: `http://localhost:5000`

### Success! 🎉

---

## USING THE APPLICATION

### Option 1: Upload CSV File
1. Click the "Upload CSV" tab
2. Click "Choose File" button
3. Select `data/sample_reviews.csv` (or your own CSV)
4. (Optional) Check "Use RoBERTa" for more accurate analysis
5. Click "Analyze Reviews"
6. Wait for analysis (2-5 seconds)
7. View results with charts and recommendations!

### Option 2: Manual Text Input
1. Click the "Manual Input" tab
2. Enter reviews separated by new lines:
   ```
   Great product! Very satisfied!
   Not as expected. Poor quality.
   Amazing! Highly recommend!
   ```
3. Click "Analyze Reviews"
4. View instant results!

### Download Sample CSV
1. Click "Download Sample CSV" button
2. This gives you a CSV file with 20 sample reviews
3. Upload it to see how the system works!

---

## EXPECTED RESULTS

### What You'll See
- **Sentiment Breakdown**: Positive %, Negative %, Neutral %
- **Pie Chart**: Visual representation of sentiment distribution
- **Individual Reviews**: Each review with its sentiment score
- **Product Recommendations**: Best products based on reviews
- **Filters**: Filter reviews by sentiment type

### Example Analysis
```
Sample Input: 20 reviews
    ↓
Processing (NLTK + VADER)
    ↓
Results:
  - Positive: 50% (10 reviews)
  - Negative: 25% (5 reviews)
  - Neutral: 25% (5 reviews)
  - Average Score: 0.245
  - Top Product: Laptop A (75% positive)
```

---

## TROUBLESHOOTING

### Problem: "Python not found"
**Solution**: Make sure Python 3.10+ is installed
- Windows: Download from python.org and check "Add Python to PATH"
- Mac/Linux: `brew install python3` or `apt install python3.10`

### Problem: "Port 5000 in use"
**Solution**: Change the port in app.py
- Open app.py
- Find the last line: `app.run(debug=True, host='0.0.0.0', port=5000)`
- Change `5000` to `5001` or another number
- Save and run again

### Problem: "Module not found"
**Solution**: Make sure virtual environment is activated
- You should see `(venv)` in your terminal
- If not, run: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)

### Problem: "NLTK data not found"
**Solution**: Download it again
```bash
python -m nltk.downloader punkt stopwords vader_lexicon
```

### Problem: Application crashes on analysis
**Solution**: Check the console for errors
- The error message will tell you what's wrong
- Most common: Missing NLTK data (see above)

---

## STOPPING THE APPLICATION

To stop the application:

**Windows**: Press `Ctrl + C` in Command Prompt
**Mac/Linux**: Press `Ctrl + C` in Terminal

You should see:
```
KeyboardInterrupt
 * Shutting down
```

---

## CUSTOMIZATION IDEAS

### Add Your Own Reviews
Create a CSV file with columns: `product,review`
```csv
product,review
MyProduct,Excellent quality!
MyProduct,Great value for money.
CompetitorX,Not satisfied.
```

### Change Sentiment Thresholds
Edit `utils/sentiment_analyzer.py`:
- Make it stricter: `if compound >= 0.1` instead of `0.05`
- Make it looser: `if compound >= 0` 

### Change Visualization Colors
Edit `visualizations.py`:
- Change color from `#2ecc71` (green) to your preferred color

### Add Database Support
Edit `app.py` to integrate SQLite or PostgreSQL for persistent storage

---

## NEXT STEPS

After your first analysis:

1. ✅ Try uploading your own CSV file
2. ✅ Test manual text input with your reviews
3. ✅ Download results as JSON
4. ✅ Explore the code in the `utils` folder
5. ✅ Read the README.md for advanced features
6. ✅ Customize the styling (CSS)
7. ✅ Add new features based on your needs
8. ✅ Deploy to cloud (Heroku, AWS, Azure)

---

## QUICK REFERENCE COMMANDS

### Activate Environment
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### Deactivate Environment
```bash
deactivate
```

### Install Packages
```bash
pip install package-name
```

### Update Requirements
```bash
pip freeze > requirements.txt
```

### Run Application
```bash
python app.py
```

### Stop Application
```bash
Ctrl + C
```

---

## FILE STRUCTURE REFERENCE

```
Your Project Folder:
├── app.py                  (Main application)
├── visualizations.py       (Charts)
├── requirements.txt        (Dependencies)
├── templates/              (HTML files)
├── static/                 (CSS & JavaScript)
├── utils/                  (Processing modules)
├── data/                   (Sample CSV)
└── README.md               (Full documentation)
```

---

## GETTING HELP

### Check These Files First:
1. **README.md** - Full documentation (500+ lines)
2. **QUICKSTART.py** - Quick reference
3. **PROJECT_SUMMARY.md** - Project overview
4. **Code comments** - Every function has comments

### Common Issues:
- **ImportError**: Run `pip install -r requirements.txt`
- **Port error**: Change port in app.py (line with `port=5000`)
- **NLTK error**: Run `python -m nltk.downloader punkt stopwords vader_lexicon`

### External Resources:
- Flask Docs: https://flask.palletsprojects.com/
- NLTK Docs: https://www.nltk.org/
- Python Docs: https://docs.python.org/3/

---

## CHECKLIST BEFORE STARTING

- ✅ Python 3.10+ installed
- ✅ Project folder accessible
- ✅ Command prompt/Terminal available
- ✅ Internet connection (for package downloads)
- ✅ ~500MB disk space available
- ✅ Web browser available (Chrome, Firefox, Safari, Edge)

---

## SUCCESS INDICATORS

You'll know everything is working when:

1. ✅ Virtual environment activates (shows `(venv)`)
2. ✅ Dependencies install without errors
3. ✅ `python app.py` shows "Running on http://127.0.0.1:5000"
4. ✅ Browser opens the homepage
5. ✅ You can upload CSV or enter text
6. ✅ Analysis completes and shows results
7. ✅ Charts display correctly
8. ✅ You see sentiment percentages and recommendations

---

## PERFORMANCE EXPECTATIONS

- **Startup time**: 5-10 seconds (first time loading NLTK data)
- **Analysis time**: 1-3 seconds for 10-100 reviews (VADER)
- **Analysis time**: 10-30 seconds for 10-100 reviews (RoBERTa)
- **Memory usage**: ~200MB baseline

---

🎉 **You're ready to go! Enjoy analyzing reviews!** 🎉

If you have questions, check the README.md or inline code comments.

Happy analyzing! 🚀
