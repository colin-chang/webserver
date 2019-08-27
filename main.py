from ColinFramework import ColinFramework
from ColinServer import ColinServer
import logging

# 路由表
_route_list = {}


def route(path):
    """路由装饰器"""

    def inner_route(func):
        _route_list[path] = func

        def new_func():
            return func()

        return new_func

    return inner_route


@route("/")
def index(env, start_response):
    start_response(ColinFramework.OK, [("Content-Type", "text/html")])
    return b"<h1>welcome</h2>"


@route("/greet")
def greet(env, start_response):
    start_response(ColinFramework.OK, [])
    return ("hi %s" % env.get("name", "there") if env else "there").encode()


def main():
    # 设置全局日志格式
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    app = ColinFramework(_route_list)  # 使用Web框架创建应用
    server = ColinServer(app)  # 使用Web服务器托管Web应用
    server.start()  # 启动Web服务器


if __name__ == '__main__':
    main()
