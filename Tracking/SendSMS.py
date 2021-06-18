from twilio.rest import Client

def sendSMS(PhoneNum, Msg) :
    account_sid = "AC6c6be62a43ab5cb4cf9ebd94278fec75"
    auth_token = "d1e688ab0560c7b2f77f80820f8e2040"

    client = Client(account_sid, auth_token)
    PhoneNum = "+91" + PhoneNum
    message = client.messages.create(body=Msg, from_="+13072249438", to=[PhoneNum])
    print(message.sid)