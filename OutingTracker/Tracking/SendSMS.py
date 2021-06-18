from twilio.rest import Client

def sendSMS(PhoneNum, Msg) :
    account_sid = "*************************************"
    auth_token = "************************************"

    client = Client(account_sid, auth_token)
    PhoneNum = "+91" + PhoneNum
    message = client.messages.create(body=Msg, from_="+13072249438", to=[PhoneNum])
    print(message.sid)
