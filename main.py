import discord

import os
from dotenv import load_dotenv

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
# 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 指定のチャンネルのみコマンド実行できるようにする
    if message.channel.id != int(os.environ["CHANNEL_ID"]):
        return
                
    if message.content == '/hello':

        text = "こんにちは"
        embed = discord.Embed(title="あいさつ",description=text, color=0x87CEEB)
        await message.channel.send(embed=embed)
            
        return

load_dotenv()

client.run(os.environ['TOKEN'])
