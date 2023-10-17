from telethon import TelegramClient

# API ID и API HASH можно получить здесь - https://my.telegram.org/auth?to=apps

api_hash = "ЗДЕСЬ ВВЕСТИ API HASH"
api_id = "ЗДЕСЬ ВВЕСТИ API ID"

client = TelegramClient("test", api_id, api_hash)

channel = "ссылка на телеграм канал"

# получить ID телеграм канала - раскоментить и запустить один раз

# async def main():
#   try:
#     info = await client.get_entity(channel)
#     print(f"{channel}    -100{info.id}")
#   except Exception as e:
#     print(f"Error with {channel}")

# здесь вставить полученный id нужного канала
telegram_chat_id = ""


async def main():
  async for message in client.iter_messages(telegram_chat_id, limit=10):
    print(message)

with client:
  client.loop.run_until_complete(main())
