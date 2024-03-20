import threading
import machine_translation_python_demo as translation


# work Thread

class workThread(threading.Thread):
    def __init__(self, jobid, text, froml, tol, child):
        super().__init__()
        self.job = jobid
        self.text = text
        self.froml = froml
        self.tol = tol
        self.child = child

    def run(self):
        # job
        item = translation.translate(self.text, fromlangu=self.froml, tolangu=self.tol)
        self.child.text = item

