import asyncio
import aioprocessing
async def child_recv():
    msg = await child_pipe.coro_recv()
    print(msg)
    
parent_pipe, child_pipe = aioprocessing.AioPipe()
parent_pipe.send("Eat shit")
  
asyncio.run(child_recv())
