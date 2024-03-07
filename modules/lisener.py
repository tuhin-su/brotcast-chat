import threading
from modules.RX import RX

class server_demon(threading.Thread):
    def __init__(self, rx: RX):
        super().__init__()
        self._stop_event = threading.Event()
        self.rx=rx

    def run(self):
        self.rx.bind()

    def stop(self):
        self._stop_event.set()