import sys
import time
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# O arquivo que será monitorado
MODULE_NAME = "main.py"  # Nome do arquivo Python sem ".py"

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, module_name):
        self.module_name = module_name

    def on_modified(self, event):
        if event.src_path.endswith(f"{self.module_name}.py"):
            print(f"Arquivo {self.module_name}.py modificado! Recarregando...")
            try:
                importlib.reload(sys.modules[self.module_name])
            except Exception as e:
                print(f"Erro ao recarregar o módulo: {e}")

if __name__ == "__main__":
    observer = Observer()
    handler = ReloadHandler(MODULE_NAME)
    observer.schedule(handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
