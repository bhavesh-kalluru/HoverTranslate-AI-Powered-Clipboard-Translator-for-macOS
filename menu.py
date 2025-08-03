import rumps
import time
import pyperclip
from threading import Thread
from translate.engine import translate_text

class HoverTranslateApp(rumps.App):
    def __init__(self):
        super().__init__("HoverTranslate", icon=None, menu=[
            "Target Language",
            "Spanish",
            "Hindi",
            "French",
            None,
            "Quit"
        ])
        self.last_clipboard = ""
        self.target_lang = None
        self.menu["Spanish"].state = False
        self.menu["Hindi"].state = False
        self.menu["French"].state = False

        self.thread = Thread(target=self.monitor_clipboard)
        self.thread.daemon = True
        self.thread.start()

    def monitor_clipboard(self):
        while True:
            try:
                if self.target_lang:
                    current = pyperclip.paste()
                    if current != self.last_clipboard and current.strip():
                        self.last_clipboard = current
                        translated = translate_text(current, "auto", self.target_lang)
                        rumps.notification(
                            title=f"Translation to {self.target_lang}",
                            subtitle="Translated Text",
                            message=translated
                        )
            except Exception as e:
                print("Clipboard error:", e)
            time.sleep(3)

    @rumps.clicked("Spanish")
    def set_spanish(self, _):
        self.target_lang = "Spanish"
        self._update_language_menu("Spanish")

    @rumps.clicked("Hindi")
    def set_hindi(self, _):
        self.target_lang = "Hindi"
        self._update_language_menu("Hindi")

    @rumps.clicked("French")
    def set_french(self, _):
        self.target_lang = "French"
        self._update_language_menu("French")

    def _update_language_menu(self, selected):
        for lang in ["Spanish", "Hindi", "French"]:
            self.menu[lang].state = (lang == selected)

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()
