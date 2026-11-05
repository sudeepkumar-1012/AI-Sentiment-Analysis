#!/usr/bin/env python
"""
Smart Review Analyzer - Installation & Setup Guide
This script helps with initial setup
"""

import os
import sys
import subprocess
import platform


def print_header(title):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def print_step(step_num, title, commands=None):
    """Print formatted step"""
    print(f"\n[Step {step_num}] {title}")
    if commands:
        for cmd in commands:
            print(f"    $ {cmd}")


def is_windows():
    """Check if running on Windows"""
    return platform.system() == "Windows"


def is_macos():
    """Check if running on macOS"""
    return platform.system() == "Darwin"


def setup_wizard():
    """Interactive setup wizard"""
    print_header("Smart Review Analyzer - Setup Wizard")
    
    print("""
This wizard will help you set up the application.

Requirements:
  • Python 3.10 or higher
  • pip (Python package manager)
  • ~500MB disk space for dependencies
    """)
    
    # Step 1: Check Python
    print_step(1, "Verify Python Installation")
    print(f"    Python version: {sys.version}")
    
    if sys.version_info < (3, 10):
        print("    ❌ ERROR: Python 3.10+ required")
        return False
    print("    ✓ Python version OK")
    
    # Step 2: Create venv
    print_step(2, "Create Virtual Environment")
    
    if is_windows():
        venv_cmd = "python -m venv venv"
        activate_cmd = "venv\\Scripts\\activate"
    else:
        venv_cmd = "python3 -m venv venv"
        activate_cmd = "source venv/bin/activate"
    
    print(f"    Command: {venv_cmd}")
    
    if not os.path.exists("venv"):
        try:
            subprocess.run(venv_cmd, shell=True, check=True)
            print("    ✓ Virtual environment created")
        except subprocess.CalledProcessError:
            print("    ❌ Failed to create virtual environment")
            return False
    else:
        print("    ℹ Virtual environment already exists")
    
    # Step 3: Activate and install
    print_step(3, "Install Dependencies")
    
    if is_windows():
        pip_install = "venv\\Scripts\\pip install -r requirements.txt"
    else:
        pip_install = ". venv/bin/activate && pip install -r requirements.txt"
    
    print(f"    Command: {pip_install}")
    print("    This may take a few minutes...")
    
    try:
        if is_windows():
            subprocess.run(f"venv\\Scripts\\pip install -r requirements.txt", shell=True, check=True)
        else:
            subprocess.run(f"bash -c 'source venv/bin/activate && pip install -r requirements.txt'", shell=True, check=True)
        print("    ✓ Dependencies installed")
    except subprocess.CalledProcessError:
        print("    ❌ Failed to install dependencies")
        return False
    
    # Step 4: Download NLTK data
    print_step(4, "Download NLTK Data")
    print("    This will download necessary NLP data (one-time)...")
    
    try:
        if is_windows():
            subprocess.run(
                'venv\\Scripts\\python -c "import nltk; nltk.download(\'punkt\'); nltk.download(\'stopwords\'); nltk.download(\'vader_lexicon\')"',
                shell=True,
                check=False
            )
        else:
            subprocess.run(
                'bash -c "source venv/bin/activate && python -c \'import nltk; nltk.download(\\\"punkt\\\"); nltk.download(\\\"stopwords\\\"); nltk.download(\\\"vader_lexicon\\\")\'"',
                shell=True,
                check=False
            )
        print("    ✓ NLTK data downloaded")
    except Exception as e:
        print(f"    ⚠ Warning: {e}")
    
    # Summary
    print_header("Setup Complete!")
    
    print("""
✓ Setup completed successfully!

Next steps:

1. Activate virtual environment:
""")
    if is_windows():
        print("     venv\\Scripts\\activate")
    else:
        print("     source venv/bin/activate")
    
    print("""
2. Run the application:
     python app.py

3. Open browser and visit:
     http://localhost:5000

4. Download sample CSV:
     Click "Download Sample CSV" on the home page

5. Upload and analyze reviews

For more information, see README.md
    """)
    
    return True


def manual_setup_guide():
    """Print manual setup guide"""
    print_header("Manual Setup Guide")
    
    print("""
If the wizard doesn't work, follow these steps manually:

WINDOWS:
--------
1. Open Command Prompt (cmd)
2. Navigate to project folder:
   cd path\\to\\smart-review-analyzer

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   venv\\Scripts\\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Download NLTK data:
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"

7. Run the app:
   python app.py

8. Open browser: http://localhost:5000


macOS / LINUX:
--------------
1. Open Terminal
2. Navigate to project folder:
   cd path/to/smart-review-analyzer

3. Create virtual environment:
   python3 -m venv venv

4. Activate virtual environment:
   source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Download NLTK data:
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"

7. Run the app:
   python app.py

8. Open browser: http://localhost:5000


TROUBLESHOOTING:
----------------
• If port 5000 is in use, modify app.py and change port number
• If NLTK data fails, try: python -m nltk.downloader punkt stopwords vader_lexicon
• If pip fails, try: python -m pip install --upgrade pip
• For permission errors, use: pip install --user -r requirements.txt
    """)


def main():
    """Main function"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║  Smart Review Analyzer & Product Recommendation System          ║
║                     Setup & Installation                         ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    print("""
Choose an option:
  1. Run setup wizard (automated)
  2. Show manual setup guide
  3. Check setup status
  4. Exit
    """)
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        success = setup_wizard()
        sys.exit(0 if success else 1)
    elif choice == "2":
        manual_setup_guide()
    elif choice == "3":
        subprocess.run([sys.executable, "setup_check.py"], check=False)
    elif choice == "4":
        print("\nGoodbye!")
    else:
        print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
