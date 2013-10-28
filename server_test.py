from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
# from flask.ext.restful import Resource, Api
from fb_login import app




# class MainHandler(RequestHandler):
#     def get(self):
#         self.write("This message comes from Tornado ^_^")
# #         api.add_resource(Login, '/login/<string:user_token>')

tr = WSGIContainer(app)

application = Application([
# (r"'/login/<string:user_token>'", MainHandler),
(r".*", FallbackHandler, dict(fallback=tr)),
])

if __name__ == "__main__":
    application.listen(8008) 
    IOLoop.instance().start() 