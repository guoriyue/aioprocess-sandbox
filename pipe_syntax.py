import asyncio
import aioprocessing
async def child_recv():
    msg = await child_pipe.coro_recv()
    return msg
    
parent_pipe, child_pipe = aioprocessing.AioPipe()
parent_pipe.send("Eat shit")
  
msg = asyncio.run(child_recv())
print(msg)

msg = asyncio.run(child_recv())
