import requests
import html
from twilio.rest import Client

STOCK = "JNJ"
COMPANY_NAME = "Johnson & Johnson"

STOCK_ENDPOINT = ""
NEWS_ENDPOINT = ""
ALPHAADVANTAGE_API = ""
NEWS_API = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

VIRTUAL_TWILIO_NUMBER = ""
VERIFIED_NUMBER = ""

yesterday_close_price = None
day_before_yesterday_close_price = None
headline = None
brief = None


def get_stock_data():
    global yesterday_close_price, day_before_yesterday_close_price
    stock_data_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": ALPHAADVANTAGE_API,
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_data_parameters)
    response.raise_for_status()
    stock_data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in stock_data.items()]
    data_list_sliced = data_list[:2]
    print(data_list_sliced)
    yesterday_close_price = float(data_list_sliced[0]["4. close"])
    day_before_yesterday_close_price = float(data_list_sliced[1]["4. close"])


def get_news_data():
    global brief, headline
    news_api_parameters = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API,
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
    news_data = response_news.json()
    headline = html.unescape(news_data["articles"][0]["title"])
    brief = html.unescape(news_data["articles"][0]["description"])
    print(headline, brief)


def send_message(char):
    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{STOCK}: {char} {percentage}%\nHeadline: {headline}\nBrief:{brief}",
        from_=VIRTUAL_TWILIO_NUMBER,
        to=VERIFIED_NUMBER,
    )

    print(message.status)


get_stock_data()
get_news_data()


differce = abs(yesterday_close_price - day_before_yesterday_close_price)
percentage = round((differce / yesterday_close_price * 100), 2)


if yesterday_close_price > day_before_yesterday_close_price:
    send_message(char="🔺")
else:
    send_message(char="🔻")
