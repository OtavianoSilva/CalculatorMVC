from tkinter import *

class View(Tk):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

    def main(self):
        self.mainloop()