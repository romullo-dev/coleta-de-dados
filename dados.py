import os
import time
from PIL import ImageGrab

def capture_screenshots(interval, count, save_directory):
    for i in range(count):
        screenshot = ImageGrab.grab()  
        timestamp = int(time.time())  
        filename = os.path.join(save_directory, f"screenshot_{timestamp}_{i + 1}.png")
        screenshot.save(filename)
        print(f"Captura salva: {filename}")
        time.sleep(interval)

save_directory = r"C:\Users\Romul\OneDrive\Área de Trabalho\fotos"  
capture_screenshots(interval=5, count=10, save_directory=save_directory)
