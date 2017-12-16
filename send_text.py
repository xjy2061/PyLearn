from twilio.rest import Client
import twilio_account


client = Client(twilio_account.account_sid, twilio_account.auth_token)

message = client.messages.create(
    to="+8618668168736",
    from_="+12028738892 ",
    body="Hello xjy2061!")

print(message.sid)
