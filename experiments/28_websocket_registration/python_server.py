# #!/usr/bin/env python
#
# # WS server example that synchronizes state across clients
#
# import asyncio
# import json
# import logging
# import websockets
#
# # logging.basicConfig()
# #
# # count = 4
# # user = {'value': 'User ' + str(count)}
# #
# connected = {}
#
#
# async def state_event():
#     return json.dumps({'type': 'username', **user})
#
#
# async def register(websocket):
#     global connected
#     # lock name
#     connected[websocket] = user
#     # unlock
#
#
# async def handler(websocket, path):
#     # Register.
#     await register(websocket)
#     try:
#         # Implement logic here.
#         await asyncio.wait([ws.send(user['value']) for ws in connected])
#         print("Hello! " + str(connected[websocket]))
#         await asyncio.sleep(10)
#     # try:
#     #     await websocket.send(state_event())
#     #     async for message in websocket:
#     #         data = json.loads(message)
#     #         if data['action'] == 'register':
#     #             print('Hello! '+str(user['value']))
#     #         else:
#     #             await asyncio.wait([ws.send(user['value']) for ws in connected])
#     #             print('Enter username')
#     finally:
#         # Unregister.
#         print('Time is up!')
#         # connected.remove(websocket)
#
# asyncio.get_event_loop().run_until_complete(
#     websockets.serve(handler, 'localhost', 6789))
# asyncio.get_event_loop().run_forever()

