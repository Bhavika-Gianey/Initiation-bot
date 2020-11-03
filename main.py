import requests as requests

url="https://api.telegram.org/bot1121443840:AAHrLOegV_syeeY18kikbFDz1BjLrGA0sOU/"



#create function that get chat id
def get_chat_id(update):
    chat_id=update['message']["chat"]["id"]
    return chat_id


#create function that gets message text
def get_messsage_text(update):
    message_text=update['message']["text"]
    return message_text


#create function that gets last update
def last_update(req):
    response=requests.get(req + "getUpdates")
    response=response.json()
    result=response["result"]
    total_updates=len(result)-1
    return result(total_updates) #get last record message update


#create function that let bot send message to the user
def send_msg(chat_id,msg_text):
    parameters={"chat_id":chat_id,"text":msg_text}
    response=requests.post(url + "sendMessage", data=parameters)
    return response
#create main function for navigate or reply message back
def main():
    update_id=last_update(url)["update_id"]
    while True:
        update=last_update(url)
        if update_id==update["update_id"]:
            if get_messsage_text(update).lower() =="hi" or get_messsage_text(update).lower()=="hello":
                send_msg(get_chat_id(update), "this form will assist you about general faq's")












