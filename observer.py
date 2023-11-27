class Observer:
    def __init__(self):
        self.subscriber = []
        self.msg = ""

    def notify(self):
        for sub in self.subscriber:
            sub.msg = self.msg

    def register(self, observer):
        self.subscriber.append(observer)

    def unregister(self, observer):
        self.subscriber.remove(observer)

class subscriber:

    def __init__(self):
        msg = ""

    def update(self):
        print(self.msg)

class Subject:
    def __init__(self):
        self.observer = []

    def notify_observer(self, info):
        for obs in self.observer:
            obs.msg = info

    def attach(self, observer):
        self.observer.append(observer)

    def dettach(self, observer):
        self.observer.remove(observer)