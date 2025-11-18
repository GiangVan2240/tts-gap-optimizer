import tkinter as tk
import logging
from queue import Queue, Empty

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("TTS Gap Optimizer")
        self.queue = Queue()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to TTS Gap Optimizer")
        self.label.pack(pady=10)

        self.run_button = tk.Button(self.master, text="Run", command=self.run)
        self.run_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def run(self):
        self.queue.put("Processing started")
        self.process_queue()

    def process_queue(self):
        try:
            while True:
                message = self.queue.get_nowait()
                logger.info(message)
                self.queue.task_done()
        except Empty:
            pass

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()