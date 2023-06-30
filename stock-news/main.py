import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

ALPHA_ADAVANTAGE_API_KEY = os.getenv("ALPHA_ADAVANTAGE_API_KEY")
NEWS_API = os.getenv("NEWS_API")
TWILIO_SID = os.getenv("twilio_sid")
TWILIO_AUTH_TOKEN = os.getenv("173fa57db8f99c5d6c5090d15b847fb4")
TO_PHONE = os.getenv('to_phone')
FROM_PHONE = os.getenv('from_phone')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol' : STOCK_NAME,
    'apikey' : ALPHA_ADAVANTAGE_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_api_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

dates = [key for key in data.keys()]

def closing_price(date):
    return float(data[date]['4. close'])

price_change = closing_price(dates[0]) - closing_price(dates[1])
percent_diff = (abs(price_change)/closing_price(dates[1]))*100

if percent_diff>0.1:
    if price_change<0:
        symbol = "🔻"
    else: 
        symbol = "🔺"

    news_pramaters = {
        'q' : COMPANY_NAME,
        'from': f"{dates[2]}",
        'to': f"{dates[0]}",
        'sortBy' : 'popularity',
        'searchIn' : 'title',
        'apikey' : NEWS_API,
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_pramaters)
    response.raise_for_status()
    articles = response.json()["articles"]
    message = f"{STOCK_NAME}: {symbol}{round(percent_diff,2)}%\nHeadline: {articles[0]['title']}.\nBrief: {articles[0]['description']}\nHeadline: {articles[1]['title']}.\nBrief: {articles[1]['description']}"
    print(message)

    # sending message
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
    from_=FROM_PHONE,
    body=message,
    to=TO_PHONE
    )



# message format is like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

