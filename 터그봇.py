import discord
import random
import os

client = discord.Client()

access_token = os.environ["BOT_TOKEN"]
token = "access_token"

@client.event
async def on_ready():

    print(client.user.name)
    print(client.user.id)
    print('[login success!]')
    print('========================')
    game = discord.Game("츄르 달라고")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("+청소"):
        numebr = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=numebr)
        await message.channel.send(f"{numebr}개의 메시지를 냥이가 삭제 했따!✅")

    if message.content == "냥아":
        ran = random.randint(1,4)
        if ran == 1:
            a = "***why?***🤔"
        if ran == 2:
            a = "***웅?***🤔"
        if ran == 3:  
            a = "***왜 구랭?***😄"
        if ran == 4:
            a = "***왜 불러?***😀"   
        await message.channel.send(a)

    if message.content == "냥아 뭐해?":
        ran = random.randint(1,3)
        if ran == 1:
            c = "***게임!***🎮"
        if ran == 2:
            c = "***프로그래밍!***💻"
        if ran == 3:  
            c = "***츄르 먹는다! 헤헤***🐱"
        await message.channel.send(c)

    if message.content == "냥이 바보":
        ran = random.randint(1,4)
        if ran == 1:
            e = "***머라구!?***😡"
        if ran == 2:
            e = "***흥-_-***😑"
        if ran == 3:  
            e = "🖕***(?)***"
        if ran == 4:
            e = "***너도 바부야...***😢"   
        await message.channel.send(e) 

    if message.content == "냥아 잘자":
        ran = random.randint(1,2)
        if ran == 1:
            f = "***웅 너두***👋"
        if ran == 2:  
            f = "***너도 잘자***👋"
        
        await message.channel.send(f)             

client.run(token)

