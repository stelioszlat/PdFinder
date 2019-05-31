import threading
from Core.extract import extract_text

class Extract_thread(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print("Thread " + id + "started")
        extract_text(id)
