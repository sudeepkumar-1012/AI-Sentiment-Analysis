#!/usr/bin/env python
"""
Smart Review Analyzer - Setup Helper Script
Validates project setup and environment
"""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.10+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Python 3.10+ required (found {version.major}.{version.minor})")
        return False
    print(f"✓ Python {version.major}.{version.minor} detected")
    return True


def check_project_structure():
    """Verify project structure"""
    required_files = [
        'app.py',
        'visualizations.py',
        'requirements.txt',
        'README.md',
        'templates/base.html',
        'templates/index.html',
        'templates/results.html',
        'templates/error.html',
        'static/css/style.css',
        'static/js/script.js',
        'utils/preprocessing.py',
        'utils/sentiment_analyzer.py',
        'utils/recommendation_engine.py',
        'data/sample_reviews.csv',
    ]
    
    missing = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing.append(file_path)
    
    if missing:
        print(f"❌ Missing files:")
        for f in missing:
            print(f"   - {f}")
        return False
    
    print("✓ Project structure is complete")
    return True


def check_dependencies():
    """Check if required packages are installed"""
    required = ['flask', 'pandas', 'nltk', 'matplotlib', 'PIL']
    
    try:
        import pip
        installed_packages = {pkg.key: pkg for pkg in pip.get_installed_distributions()}
    except:
        # For newer pip versions
        from importlib.metadata import distributions
        installed_packages = {d.name.lower(): d for d in distributions()}
    
    missing = []
    for package in required:
        if package.lower() not in str(installed_packages).lower():
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    print("✓ All dependencies installed")
    return True


def check_nltk_data():
    """Check if NLTK data is downloaded"""
    try:
        import nltk
        import nltk.data
        
        required_data = [
            'tokenizers/punkt',
            'corpora/stopwords',
            'sentiment/vader_lexicon'
        ]
        
        missing = []
        for data in required_data:
            try:
                nltk.data.find(data)
            except LookupError:
                missing.append(data)
        
        if missing:
            print(f"⚠ Missing NLTK data: {', '.join(missing)}")
            print("  Run: python -c \"import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')\"")
            return False
        
        print("✓ NLTK data is available")
        return True
    except Exception as e:
        print(f"⚠ Could not check NLTK data: {e}")
        return False


def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("Smart Review Analyzer - Setup Verification")
    print("="*60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Project Structure", check_project_structure),
        ("Dependencies", check_dependencies),
        ("NLTK Data", check_nltk_data),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n[{name}]")
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    if all(results):
        print("✓ All checks passed! Ready to run.")
        print("\nTo start the application:")
        print("  python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\nFor installation help, see README.md")
    print("="*60 + "\n")
    
    return all(results)


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
