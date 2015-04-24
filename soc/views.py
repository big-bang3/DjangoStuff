from django.shortcuts import render_to_response
import socket
from django.http.response import HttpResponse
from django.template import RequestContext
# Create your views here.


def sock(request, word):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5567
    my_l = []
    host = '127.0.0.1'
    if word == 'server':
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        while True:
            sc, addrs = s.accept()
            print("Connection from : ", addrs)
            my_l.append(addrs)
            for i in my_l:
                print(i)
            m = sc.recv(100)
            print("Message recieved : ", m)
    elif word == 'client':
        s.connect((host, port))
        m = ''
        s.send(bytes("Hello server", "utf-8"))
        return HttpResponse("<html>Connection succesful</html>")
    elif word == 'close':
        s.close()
        return HttpResponse("<html>Connection CLosed</html>")
        