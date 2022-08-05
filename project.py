"""
* CS50P Final project
* Final Project Representer
* by Samu Reinikainen 05.08.2022
"""

from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3
import time
import ast
import argparse

class Fpr:
    def __init__(self, title, width=1024, height=768):
        self.engine = init_speak()
        self.w = tk.Tk()
        self.w.geometry(f"{width}x{height}")
        self.width = width
        self.height = height
        self.w.title(title)

        self.c = tk.Canvas(self.w, bg = '#f0d8c5')
        self.c.pack(fill="both", expand=True)

        font = "Times 60 italic bold"
        self.ctitle = self.c.create_text(self.width/2, 100, fill="#111354", font=font, justify="center")

        font = "Times 30"
        self.ctext = self.c.create_text(self.width/2, 300, fill="#111354", font=font, justify="center", width=self.width-20)

    def slideshow(self, slides):
        for slide in slides:
            speak = slide.get("speak", False)
            title = slide.get("title", False)
            text = slide.get("text", False)
            image = slide.get("image", False)
            pause = slide.get("pause", 0)

            self.view_slide(title, text, image, speak)

            time.sleep(pause)

    def view_slide(self, title, text, image, speak=False):
        if title != False:
            self.c.itemconfig(self.ctitle, text=title)
        if text != False:
            self.c.itemconfig(self.ctext, text=text)
        if image:
            img = get_pimage(get_image(image))
            if img:
                self.c.create_image(self.width/2, 240, anchor="n", image=img)
        self.c.update()

        if speak:
            say(self.engine, speak)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default="script.txt", help="Script filename", type=str)
    parser.add_argument("-ww", default=1024, help="Window width", type=int)
    parser.add_argument("-wh", default=768, help="Window height", type=int)
    args = parser.parse_args()

    slides = get_script(args.f)

    fpr = Fpr("Final Project Representer", args.ww, args.wh)
    fpr.slideshow(slides)
    fpr.w.mainloop()

def get_image(filen: str) -> object:
    """
    Open filepath and return PIL image object.

    :param filen: filepath
    :type filen: str
    :return: PIL image object
    :rtype: object
    """
    if filen:
        try:
            Image.open(filen)
        except FileNotFoundError:
            return False

def get_pimage(img: object) -> object:
    """
    Open filepath and return tkinter photoimage object.

    :param img: pillow image object
    :type filen: object
    :return: Photoimage image object
    :rtype: object
    """
    if img:
        try:
            return ImageTk.PhotoImage(img)
        except:
            return False

def get_script(filen: str) -> dict:
    """
    Open filepath and return script as dictionary.

    :param filen: filepath
    :type filen: str
    :exit: If filen is not found or file is not valid
    :return: script as dictionary
    :rtype: dict
    """

    if filen:
        try:
            with open(filen, "r") as file:
                script = file.read().replace('\n', '')
        except FileNotFoundError:
            exit("Error: script file not found")
        except UnicodeDecodeError:
            exit("Error: script file not valid file")

        try:
            return ast.literal_eval(script)
        except SyntaxError:
            exit("Error: script syntax malformed")

def init_speak() -> object:
    """
    Initialize speach synthetizer

    :raise Error: If speach synthetizer not found
    :return: Pyttsx3 speach engine
    :rtype: object
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("voice", "english-us+f5")
        #engine.setProperty("voice", "finnish")

        return engine
    except:
        exit("Error: speach synthetizer not found")

def say(engine: object, text: str):
    """
    Speak given text.

    :param engine: string to speak
    :type engine: object
    :param text: string to speak
    :type text: str
    :return: None
    """

    try:
        engine.say(text)
        engine.runAndWait()
    except:
        exit("Error: speach synthetizer not found")

if __name__ == "__main__":
    main()
