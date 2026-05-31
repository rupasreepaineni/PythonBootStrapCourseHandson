import requests

STOCK_NAME = "TSLA",
COMPANY_NAME = "Tesla Inc",

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# GUEN7VXE4G20ZHBV

Stock_params = {"function" : "TIME_SERIES_DAILY",
"symbol" : STOCK_NAME,
"apikey" : "2RNHOANFFIR97I93.",}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params=Stock_params)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#through dictionary comprehension method
# [new_value for (key, value) in dictionary.items()
previous_day_data = [(date,data['4. close']) for (date,data) in data['Time Series (Daily)'].items()]
print(previous_day_data[1])

# previous_day_data = [(last_stock['4. close']) for last_stock in data['Time Series (Daily)'].values()]
# day_before_data = previous_day_data[1]
# print(day_before_data) #list comprehension method

 #normal ftech method
# last_stock_series = data['Time Series (Daily)']
# last_stock = list(last_stock_series.values())
# print(last_stock)
# day_before_data = last_stock[1]['4. close']


#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

