import os


class ColinFramework(object):
    """自定义Web框架"""

    # 静态资源根目录
    STATIC_ROOT_PAT = "./wwwroot"
    # Http Status
    OK = "200 OK"
    NOT_FOUND = "404 Not Found"

    def __init__(self, route):
        self.__route = route  # 路由

    def __call__(self, env, start_response):
        path = env.get("path", "/")  # 当前请求路径

        # 1.请求静态资源
        mark = "/static/"
        if path.startswith(mark):
            filename = os.path.join(self.STATIC_ROOT_PAT, path[len(mark):])

            if os.path.exists(filename):
                file = open(filename, "rb")
                content = file.read()
                file.close()

                start_response(self.OK, [])
                return content
            else:
                start_response(self.NOT_FOUND, [])
                return b"Not Found"

        # 2.请求动态资源
        for url, handler in self.__route.items():
            if url == path:  # 路由分发
                return handler(env, start_response)

        start_response(self.NOT_FOUND, [])
        return b"Not Found"
