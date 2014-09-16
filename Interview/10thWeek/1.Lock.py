from threading import Thread, Lock

def f():
    while True:
        print(0)

def g():
    while True:
        print(1)

t1 = Thread(target=f)
t2 = Thread(target=g)
t1.start()
t2.start()
