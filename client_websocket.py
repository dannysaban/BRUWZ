from websocket import create_connection


ws = create_connection("ws://localhost:8188/websocket", message={"data":"young and restless"})
print "Sending 'Hello, World'..."
ws.send("Hello, Danny long time no seen ...")
print "Sent"
print "Reeiving..."
result =  ws.recv().rstrip()
print "Received '%s'" % result
ws.close()