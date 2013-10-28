import tornado.ioloop
import tornado.web
# from flask import Flask, request
# from flask.ext.restful import Resource, Api
from pyfb import Pyfb
import pymongo


# app = Flask(__name__)
# api = Api(app)

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int )

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, user_token):
        
        FACEBOOK_APP_ID = '134416106741047'

        facebook = Pyfb(FACEBOOK_APP_ID)

        #Opens a new browser tab instance and authenticates with the facebook API
        #It redirects to an url like http://www.facebook.com/connect/login_success.html#access_token=[access_token]&expires_in=0
        facebook.authenticate()

        #Copy the [access_token] and enter it below
        getToken = user_token#'CAACEdEose0cBACIgotCQGDecYsWW1O7wrc5saw0ZCxrM8nKzF3wWgIvQqGyb9H5u3MIBKak9jcYc3l1CNZCdYniVI3tweTC8vX2PdibMlJrdrH1LIeJnmgWQS8WpkXyRzY8dpvGgFDZARq2amdAZBEXEXJePKSuMqTIOXCCfQMzNd3QMtldxD25lkFg3IANRVfjviSo6uQZDZD'

        #Sets the authentication token
        facebook.set_access_token(getToken)

        #Gets info about myself
        me = facebook.get_myself()
        me_pic = facebook.fql_query('SELECT pic_small FROM user WHERE uid = me()')
        #friends = facebook.get_friends()

        me_name = me.name
        me_id = me.id
        me_gender = me.gender
        location = getattr(me, "location")
        me_location = location.name

        for i in me_pic:
            try:
                my_pic = i.pic_small
            except AttributeError:
                my_pic = 'None'
            try:
                me_birthday = me.birthday
            except AttributeError:
                me_birthday = 'None'

            try:
                me_status = me.relationship_status   
            except AttributeError:
                me_status = 'None'

            try:
                me_link = me.link
            except AttributeError:
                me_link = 'None'
    
    
        me_all = {'name': me_name, 'id': me_id, 'gender': me_gender, 'location': me_location, 'birthday': me_birthday, 'status': me_status, 'link': me_link, 'picture': my_pic  }    
        #db.dannysaban.insert(me_all)
        #print 'me - done!'
        #get_me = db.dannysaban.find({'id': me_id})
#         print me_all   
        self.write(me_all)
        self.finish()

app = tornado.web.Application([
    (r'/login/<string:user_token>', IndexHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    