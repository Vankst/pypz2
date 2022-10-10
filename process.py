import time
from sheduller import FileShedulle
from watchdog.observers import Observer

path_to_file = "file.txt"
event_handler = FileShedulle(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()