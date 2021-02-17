import sys

import tornado.ioloop
import tornado.web
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        print({os.getpid()})
        self.write("Served from: ")
        self.write(os.getpid().__str__())

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/basic", basicRequestHandler)
    ])

    port = 8882
    if (sys.argv.__len__() > 1):
        port = sys.argv[1]

    app.listen(port)
    print("Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()