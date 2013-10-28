import logging
import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=8188, help="run on the given port", type=int)

# we gonna store clients in dictionary..
clients = dict()

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("danny - This is your response")
        self.render("index2.html")
        #self.finish()
        


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    cache = []
    waiters = set()
    cache_size = 200
    
    def open(self, message='start talking...'):
        #print "danny , WebSocket opened - %s" % (Mymessage)
        self.write_message("danny , WebSocket opened - %s" % (message))
        EchoWebSocket.waiters.add(self)
        
    def write_message(self, message2, binary=False):
        print("danny's SERVER(8188) received a message -- %s" % (message2))
        
    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]
            
    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)
      
    def on_message(self, message = 'no message...'):
        chat = message #{"danny": "hello you can see me!!"}
        EchoWebSocket.send_updates(chat)
        EchoWebSocket.update_cache(chat)
        self.write_message(u"You said: %s" %(message)) 
         
     
    def on_close(self):
        print "Danny - WebSocket closed"
        
# class WebSocketHandler(tornado.websocket.WebSocketHandler):
# class EchoWebSocket(tornado.websocket.WebSocketHandler):    
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
#         
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
    
    