import discord
from discord.ext import commands


# 사용자 , 봇 정의
intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)

# 앱 실행을 위한 토큰 가져오기
def read_token():
    with open(r"D:\VScode\Discord_bot_python\token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()


# 봇 이벤트 처리
@client.event
async def on_ready():
    print(client.user.name, "has connected to Discord")
    await client.change_presence(
        status=discord.Status.online,
        activity=None
        )


# 봇 커맨드 입력
@client.command()
async def 자비스(ctx, *, text=None):
    if text != None:    # 입력값이 있을 때
        await ctx.send(text)
    if text == None:    # 입력값이 없을 때
        await ctx.send("안녕하세요")

# 봇 실행
client.run(token)