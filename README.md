# ai-web-page-summarizer
This project scrapes content from a provided webpage and generates a concise summary using natural language processing techniques.

## 🚀 Features
- Scrapes text content from any public webpage
- Generates concise summaries of the extracted content
- Simple and easy to set up

## 📦 Installation
### 1. Clone the repository
```bash
git clone https://github.com/markoristic3ap/ai-web-page-summarizer.git
cd ai-web-page-summarizer
```
### 2. Set Up a Virtual Environment (Recommended)

**MacOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```
***⚙️ Required Libraries:*** 
- ***requests*** – For sending HTTP requests
- ***python-dotenv*** – To manage environment variables securely
- ***beautifulsoup4*** – For parsing and extracting data from HTML
- ***openai*** – To interact with OpenAI’s API for text summarization

## ✅ Usage

After installing dependencies, you can run the main script:
```bash	
python main.py
```

## 🗑️ Deactivate the Virtual Environment (When Done)
```bash
deactivate
```

## 🤔 Troubleshooting
**Ensure Python is installed:**\
Check with python --version or python3 --version.

**Pip Issues:**\
If pip isn’t recognized, try python -m pip install --upgrade pip.

