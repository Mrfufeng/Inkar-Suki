from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from .mcv import *
from .mcs import *

mcbv = on_command("mcbv", priority=5) # 获取MC基岩版最新版本
@mcbv.handle()
async def _():
    msg = await mcbedrockv()
    await mcbv.finish(msg)

mcjv = on_command("mcjv", priority=5) # 获取MC Java版最新版本
@mcjv.handle()
async def _():
    msg = await mcjavav()
    await mcjv.finish(msg)
    
mcjes = on_command("jes", priority=5) # 获取MC Java版服务器信息
@mcjes.handle()
async def _(args: Message = CommandArg()):
    ip = args.extract_plain_text()
    msg = await jes(ip)
    await mcjes.finish(msg)
    
mcbes = on_command("bes", priority=5) # 获取MC 基岩版服务器信息
@mcbes.handle()
async def _(args: Message = CommandArg()):
    ip = args.extract_plain_text()
    msg = await bes(ip)
    await mcbes.finish(msg)