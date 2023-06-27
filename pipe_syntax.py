# # import subprocess
# # subprocess.__file__
# # # 启动另一个Python程序
# # process = subprocess.Popen(["python3", "/home/ubuntu/Holdem/poker.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# # # Provide input to b.py
# # input_data = input("Enter input for b.py: ")

# # # Send the input to b.py
# # process.communicate(input_data.encode())

# # output = process.stdout.read()
# # print(output.decode())
# # # Wait for the subprocess to finish
# # process.wait()

# # # # 从主程序获取输入
# # # input_data = "2"

# # # # 将输入发送给另一个Python程序
# # # process.stdin.write(input_data.encode())
# # # process.stdin.close()

# # # # 读取另一个Python程序的输出
# # # output = process.stdout.read()

# # # # 打印输出
# # # print(output.decode())

# # # # 等待另一个Python程序执行结束
# # # process.wait()

# import asyncio
# import sys

# code = """
# from holdem_act.table import *
# from holdem_act.player import *
# from holdem_act.game import *

# table = Table('tT', 1, 2, 4, 50)
# player1 = Player('p1', 300, 1)
# player2 = Player('p2', 300, 2)
# player3 = Player('p3', 300, 3)
# player4 = Player('p4', 300, 3)
# table.add_player(player1)
# table.add_player(player4)
# table.add_player(player2)
# table.add_player(player3)

# game = Game(table) 
# game.play_game()
# """

# async def interact_with_subprocess():
#     proc = await asyncio.create_subprocess_exec(
#         sys.executable, '-c', code,
#         stdin=asyncio.subprocess.PIPE,
#         stdout=asyncio.subprocess.PIPE)

#     # Read one line of output.
#     data = await proc.stdout.readline()
#     line = data.decode('ascii').rstrip()

#     # Wait for the subprocess exit.
#     await proc.wait()
    
# asyncio.run(interact_with_subprocess())
import asyncio
import aioprocessing

parent_pipe, child_pipe = aioprocessing.AioPipe()
self.parent_pipe.send(self._handle_send_message(temp_msg_id=temp_msg_id, message=message))
  
msg = await self.child_pipe.coro_recv()
