from deep_translator import GoogleTranslator
from pynput import keyboard
import pyperclip
import time
import subprocess   
import os


translator = GoogleTranslator(source='auto', target='tr')
last_cmd_time = 0
output_file = '/Users/efeemirhandogan/Documents/TranslatorApp/ceviriler.txt'

def save_on_file(text):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Clear file before write
            f.write(text + '\n')
            return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def on_press(key):
    global last_cmd_time
    try:
        if key == keyboard.Key.cmd:
            pass

        elif key.char == 'c':
            now = time.time()
            if now - last_cmd_time < 1:
                time.sleep(0.1)
                text = pyperclip.paste()
                if text.strip():
                    translated_text =  GoogleTranslator(source='auto', target='tr').translate(text)
                    print(f"Translated text: {translated_text}")
                    if save_on_file(translated_text):
                        if os.path.exists(output_file):
                            subprocess.run(['open', output_file])
            last_cmd_time = now
    except AttributeError:
        pass

def start_listener():
    print("Listener started. Press 'cmd + c + c' to translate text.")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Listener error: {e}")


if __name__ == "__main__":
    start_listener()