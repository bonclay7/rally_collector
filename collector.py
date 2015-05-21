import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):

    def prepare(self):
        content_type = self.request.headers.get("Content-Type")
        if not (content_type is None):
            if content_type.startswith("application/json"):
                self.json_args = json.loads(self.request.body)
            else:
                self.json_args = None

    def get(self):
        self.write("Hello, world \n")
        print self.request

    def post(self, *args, **kwargs):
        print self.request.headers


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()