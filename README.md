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
- ***gradio*** - Provides web interface

### 4. Set Up OpenAI API Key  
This project requires an **OpenAI API key** for text summarization.  

#### **Steps to Configure API Key:**  
1. **Obtain an API Key** from OpenAI: [OpenAI API](https://platform.openai.com/signup/)  
2. **Create a `.env` file** in the project root (or rename `.env.example` to `.env`).  
3. **Add your API key** inside `.env` like this:  
```bash
OPENAI_API_KEY=your-api-key-here
```

## ✅ Usage

After installing dependencies, you can run the main script:
```bash	
python main.py
```
![Screenshot 2025-02-16 at 20 22 38](https://github.com/user-attachments/assets/81edd0f8-a01c-4a17-8d71-9106c7c4703e)


## 🗑️ Deactivate the Virtual Environment (When Done)
```bash
deactivate
```

## 🤔 Troubleshooting
**Ensure Python is installed:**\
Check with python --version or python3 --version.

**Pip Issues:**\
If pip isn’t recognized, try python -m pip install --upgrade pip.

