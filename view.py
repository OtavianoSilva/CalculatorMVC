from tkinter import *

class View(Tk):

    PAD: int = 10

    MAX_BUTTONS_PER_ROW: int = 4

    button_captions: list = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]


    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.title('PyCalc1')

        self.value_var = StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()


    def main(self) -> None:
        self.mainloop()


    def _make_main_frame(self) -> None:
        self.main_frame = Frame(self)
        self.main_frame.pack(padx= self.PAD, pady= self.PAD)


    def _make_entry(self) -> None:
        entry = Entry(
            self.main_frame, justify= 'right', textvariable= self.value_var,
            state= 'disabled'
            )
        entry.pack(fill= 'x')

    
    def _make_buttons(self) -> None:
        frame = Frame(self.main_frame)
        frame.pack()

        row_controller = 0
        column_controller = 0

        for caption in self.button_captions:
            if column_controller == self.MAX_BUTTONS_PER_ROW:
                row_controller += 1
                column_controller = 0

            button = Button(frame, command= lambda button = caption:
                self.controller.on_button_click(button), text= caption, height= 2, width= 3
                )
            button.grid(row= row_controller, column= column_controller)

            column_controller += 1