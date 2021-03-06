import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=8088, help="run on the given port", type=int)

# we gonna store clients in dictionary..
clients = dict()

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("danny - This is your response")
        self.render("inde.html")
        #self.finish()
    def post(self):
        self.write("danny - This is your post")
        self.finish()

class EchoWebSocket(tornado.websocket.WebSocketHandler):
     
    '''
    connection with server..
    '''    
    
    def write_message(self, message, binary=True):
        print (message)   
    
#---------------------------------------------------#
    
    def open(self, message='start talking to me - all clients...'):
        print "Danny , WebSocket opened --%s" % (message)
        #self.write_message("WebSocket opened -- Helloooooooooooo you all clients - %s" % (message))    

        
    def on_message(self, message):
        print "   ::SERVER(8088) received a message from client --"
        self.write_message(u"   --Client said: %s" %(message)) 
            
    
    def on_close(self):
        print "Danny - WebSocket closed --"
        
# class WebSocketHandler(tornado.websocket.WebSocketHandler):
#     def open(self, *args):
#         self.id = self.get_argument("Id")
#         self.stream.set_nodelay(True)
#         clients[self.id] = {"id": self.id, "object": self}
#         
# 
#     def on_message(self, message):        
#         """
#         when we receive some message we want some message handler..
#         for this example i will just print message to console
#         """
#         print "danny's Client %s received a message : %s" % (self.id, message)
#          
#     def write_message(self, message, binary=False):
#         print "danny's Client %s received a message : %s" % (self.id, message)
#         
#     def on_close(self):
#         if self.id in clients:
#             del clients[self.id]

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/websocket', EchoWebSocket),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    