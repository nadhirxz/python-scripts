from telethon import TelegramClient

api_id = 0
api_hash = ""
username = ""

client = TelegramClient(username, api_id, api_hash)
async def main():
    receiver = input("To whom you want to send the message : ")
    message = input("Your message : ")
    if message=="image":
        img = input("Your image : ")
        await client.send_file(receiver, img)
    else :
        await client.send_message(receiver, message)

with client:
    client.loop.run_until_complete(main())
