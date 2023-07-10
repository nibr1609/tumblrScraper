# tumblrScraper
Scrapes Images and Text from any Tumblr Blog (and corrects it using GPT-3)
## Usage
1. Create an API Key here https://www.tumblr.com/oauth/apps (For this application Callback URL doesn't matter)
2. Put the key in the corresponding key.txt in the key folder
3. Create a venv and activate it

Unix:
```
python3 -m venv venv
source venv/bin/activate
```
Windows PowerShell:  
```
python -m venv venv
venv\Scripts\activate
```
4. Install requirements:  
`pip install -r requirements.txt`
5. Start script  
`python3 scraper.py`

## Use Correction with GPT-3
1. Create an API Key for Open AI (+ add funds)
2. Put the key in the corresponding openAIKey
3. Start script  
`python3 corrector.py`