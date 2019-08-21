from ColinFramework import ColinFramework
from ColinServer import ColinServer


class WebApp(object):

    def run(self):
        app = ColinFramework({
            "/": self.__index,
            "/greet": self.__greet
        })
        server = ColinServer(app)
        server.start()

    def __index(self, env, start_response):
        start_response(ColinFramework.OK, [("Content-Type", "text/html")])
        return b"<h1>welcome</h2>"

    def __greet(self, env, start_response):
        start_response(ColinFramework.OK, [])
        return ("hi %s" % env.get("name", "there") if env else "there").encode()


if __name__ == '__main__':
    app = WebApp()
    app.run()