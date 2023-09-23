import threading
from waitress import serve

from server import app
import server.submit_loop
import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.environ["FLASK_APP"] = "./server/standalone.py"
    thr1 = threading.Thread(target=serve, daemon=True, args=(app,), kwargs=({"host":"0.0.0.0", "port":5001}))
    thr2 = threading.Thread(target=server.submit_loop.run_loop, daemon=True)
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
