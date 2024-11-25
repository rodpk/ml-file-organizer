from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess

class OrganizeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path_endswith(('.jpg', '.jpeg', '.png')):
            subprocess.run(["python", "predict_script.py"]) ## run prediction script


# Monitor folder
to_organize_path = "/example/to-organize"
event_handler = OrganizeHandler()

observer = Observer()
observer.schedule(event_handler, path=to_organize_path, recursive=False)

print(f"Watching {to_organize_path} for new files...")
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()