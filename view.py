from tkinter import *

class View(Tk):

    PAD = 10

    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.title('PyCalc1')

        self._make_main_frame()
        self._make_entry()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        entry = Entry(self.main_frame)
        entry.pack()