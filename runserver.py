import tornado.ioloop
import tornado.web
import views

def make_app():
    return tornado.web.Application([
        (r"/get_form", views.MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()