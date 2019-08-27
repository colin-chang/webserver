from gevent import monkey, socket
from gevent import spawn

monkey.patch_all()


class ColinServer(object):
    """
    自定义Web服务器
    """

    def __init__(self, application, port=80):
        """
        初始化服务器
        :param application:WSGI Web应用程序
        :param port:监听端口
        """
        server = socket.socket()
        server.bind(('', port))
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server = server

        self.__application = application

    def start(self):
        """
        启动服务器(协程版)
        :return:
        """
        self.__server.listen()

        try:
            while True:
                client, addr = self.__server.accept()
                spawn(self.__process_request, client)  # 创建协程为客户端服务
        except:
            pass
        finally:
            self.__server.close()

    def __process_request(self, client):
        """
        处理客户端请求
        :param client:客户端连接
        :return:
        """
        request = client.recv(1024)
        if request:
            # 解析请求报文头
            request_headers = request.decode().splitlines()
            url_parts = request_headers[0].split()[1].split("?")
            path = {"path": url_parts[0]}
            params = {} if len(url_parts) < 2 else eval("{%s}" % ",".join(
                map(lambda item: ":".join(map(lambda kv: "\"{}\"".format(kv), item.split("="))),
                    url_parts[1].split("&"))))

            # 处理请求
            env = {}
            env.update(path)
            env.update(params)
            response_headers = []

            def start_response(status, headers):
                response_headers.append("HTTP/1.1 %s" % status)
                response_headers.extend(map(lambda header: "{}:{}".format(header[0], header[1]), headers))
                response_headers.append("\r\n")

            response_body = self.__application(env, start_response)
            client.send("\r\n".join(response_headers).encode() + response_body)
        client.close()
