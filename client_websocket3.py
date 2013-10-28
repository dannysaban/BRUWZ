import websocket
hostname = 'ws://localhost'
port = '8088/websocket'

ws = websocket.WebSocket()

ws.connect("%s:%s" % (hostname, port))
ws.send("Hello, Server - the client is talking: how RU?...")
ws.recv_data()
ws.close()