created my own JSON viewer using AI, 
the JSON data will be pasted in the text area and the viewer will display the data in a more readable format.
#http://127.0.0.1:5000

required URL:
https://home.openweathermap.org/users/sign_in - for api key/calls
https://openweathermap.org/api/weather-conditions#Weather-Condition-Codes-2 - for weather codes and icons


sendingsmsifitrains.py
1. Go to twilio account and login to the account
2. Go to the dashboard and click on the "Get a Trial Number" button to get a phone number for testing.
3. Go to the "Programmable SMS" section and click on the "Settings" tab.
4. Scroll down to the "Messaging Services" section and click on the "Create Messaging Service" button
5. Then Go to account dashboard we'll have the "Account SID" and "Auth Token" 
which we will use in our code to authenticate with the Twilio API.
6. and next to that there'll be quickstart docs 
7. https://www.twilio.com/docs/messaging/quickstart
8. Install flask through terminal using pip install flask
9. we'll have guide to include the code and trigger the SMS 
10.NOTE: This code isn't working due to the fact that the free trial account of twilio,
only allows you to send SMS to verified phone numbers,
so you need to verify your phone number in the twilio account before you can send SMS to it.
