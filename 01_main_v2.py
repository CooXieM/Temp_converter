import tkinter
from tkinter import *


class Converter:

    def __init__(self):

        # initialise variables such as feedback
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        button_font = ("Arial", "12", "bold")
        # set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold"),
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

        error = "Please enter a number greater than -459"
        self.temp_error = Label(self.temp_frame,
                                text="",
                                font=("Arial", "12", "bold"),
                                fg="#9C0000")

        self.temp_error.grid(row=3)

        # Button Frames

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.temp_celsius = Button(self.button_frame,
                                   text="To Celsius C",
                                   font=button_font,
                                   bg="#0080FF",
                                   width=15,
                                   command=self.to_celsius
                                   )
        self.temp_celsius.grid(row=0, column=0, padx=1, pady=1)

        self.temp_fahrenheit = Button(self.button_frame,
                                      text="To Fahrenheit F",
                                      font=button_font,
                                      bg="#FF8000",
                                      width=15,
                                      command=self.to_fahrenheit
                                      )
        self.temp_fahrenheit.grid(row=0, column=1, padx=1, pady=1)

        self.temp_help_info = Button(self.button_frame,
                                     text="Help / Info",
                                     font=button_font,
                                     bg="#00FF80",
                                     width=15
                                     )
        self.temp_help_info.grid(row=1, column=0, padx=1, pady=1)

        self.temp_history_export = Button(self.button_frame,
                                          text="History / Export",
                                          font=button_font,
                                          bg="#FF0080",
                                          width=15,
                                          state=DISABLED
                                          )
        self.temp_history_export.grid(row=1, column=1, padx=1, pady=1)

    # Check input is more than -273 // future test make it -273C and 470F
    def check_input(self, min_temp):

        has_error = "no"
        error = "Please enter a number that is more than {}".format(min_temp)

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_temp:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # if num invalid display error
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_has_error.set(error)
            return "invalid"

        else:
            # set no to previous errors
            self.var_has_error.set("no")
            # enable history
            self.temp_history_export.config(state=NORMAL)
            return response

    def to_celsius(self):
        to_convert = self.check_input(-273)

        if to_convert != "invalid":

            self.var_feedback.set(f"Converting {to_convert} to C")

        self.output_ans()

    def to_fahrenheit(self):
        to_convert = self.check_input(-459)

        if to_convert != "invalid":
            self.var_feedback.set(f"Converting {to_convert} to F")

        self.output_ans()

    def output_ans(self):
        output = self.var_feedback.get()
        has_error = self.var_has_error.get()

        if has_error == "yes":
            self.temp_error.config(fg="9C0000")
            self.temp_entry.config(bg="F8CECC")

        else:
            self.temp_error.config(fg="#004C00")
            self.temp_entry.config(bg="#ffffff")

        self.temp_error.config(text=output)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
