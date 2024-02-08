from tkinter import *


class Converter:

    def __init__(self):

        button_font = ("Arial", "12", "bold")
        # set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature in the box below " \
                       "then press one of the buttons to convert " \
                       "your temperature from Celsius or Fahrenheit"
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       )
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "12")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Error msg"
        self.temp_arg = Label(self.temp_frame,
                              text=error,
                              font=("Arial", "12", "bold"),
                              fg="#9C0000")

        self.temp_arg.grid(row=3)

        # Button Frames

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.temp_celsius = Button(self.button_frame,
                                   text="To Celsius C",
                                   font=button_font,
                                   bg="#0080FF",
                                   width=15
                                   )
        self.temp_celsius.grid(row=0, column=0)

        self.temp_fahrenheit = Button(self.button_frame,
                                      text="To Fahrenheit F",
                                      font=button_font,
                                      bg="#FF8000",
                                      width=15
                                      )
        self.temp_fahrenheit.grid(row=0, column=1)

        self.temp_help_info = Button(self.button_frame,
                                     text="Help / Info",
                                     font=button_font,
                                     bg="#00FF80",
                                     width=15
                                     )
        self.temp_help_info.grid(row=1, column=0)

        self.temp_history_export = Button(self.button_frame,
                                          text="History / Export",
                                          font=button_font,
                                          bg="#FF0080",
                                          width=15,
                                          state=DISABLED
                                          )
        self.temp_history_export.grid(row=1, column=1)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
