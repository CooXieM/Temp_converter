from tkinter import *


class Converter:
    def __init__(self):
        # sets up GUI widget
        self.temp_frame = Frame()
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter"
                                  )
        self.temp_heading.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
