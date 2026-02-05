import threading
import time
import webbrowser
from webGUI import webGUI

def open_browser(port:int):
    url = f'http://127.0.0.1:{port}'
    webbrowser.open(url)
    print(f'浏览器打开 {url} 成功')

if __name__ == '__main__':

    runport = webGUI.find_free_port()

    flask_thread = threading.Thread(target=webGUI.run, args=(runport,))
    flask_thread.daemon = True
    flask_thread.start()

    time.sleep(1)

    open_browser(runport)

    try:
        flask_thread.join()
    except KeyboardInterrupt:
        print("\n程序已手动终止")