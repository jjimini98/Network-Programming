import asyncio
from socket import *
import random

bufsize =1024


async def handler(reader, writer):
    while True:
        data = await reader.read(bufsize)
        addr = writer.get_extra_info('peername')

        if data.decode() == "1":
            temp = random.randint(0, 40)
            msg = "Temp=" + str(temp)
            writer.write(msg)
            await writer.drain()


        elif data.decode() == "2":
            humid = random.randint(0, 100)
            msg = "Humid=" + str(humid)
            writer.write(msg)
            await writer.drain()


async def main():
    server = await asyncio.start_server(handler, 'localhost', 9999)

    addr = server.sockets[0].getsockname()
    print(f'Connected from {addr}')
    await server.serve_forever()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()