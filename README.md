# Simple Web server
this is a simple demo of a basic web server and web framework under WSGI based on Python3.
it just shows how a web framework like Django work with a web server like nginx under WSGI.

We just try to explain their work process with some simple codes.The purpose of this project is just for learn and understand Python web server.


## Run
make sure you've installed `Python3` and `pip3` before runt this project.

We used [coroutine (gevent) ](https://colin-chang.site/python/senior/coroutine.html) to achieve multi-task.

```sh
pip3 install gevent
python3 main.py
```
This web server binds port 80 for default.try to change it if 80 is not available.

## Test
try to visit the urls below to check if the server works correctly.

```
http://127.0.0.1
http://127.0.0.1/static/index.html
http://127.0.0.1/static/girl.jpg
http://127.0.0.1/greet?name=colin
```
