import pyperclip

def capture_text():
    try:
        text = pyperclip.paste()
        return text.strip()
    except Exception as e:
        print("Clipboard error:", e)
        return ""
