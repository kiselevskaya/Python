#!/usr/bin/env python

# WS client example
# WSS (WS over TLS) client example, with a self-signed certificate

import asyncio
#wss
# import pathlib
# import ssl
import websockets

# wss
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# ssl_context.load_verify_locations(pathlib.Path(__file__).with_name('localhost.pem'))


async def hello():
    # wss (, ssl=ssl_context)
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
