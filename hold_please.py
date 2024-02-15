


def to_celsius(self):
    to_convert = self.check_input(-273)

    # gets input and converts it to the opposing temp and prints it
    if to_convert != "invalid":
        answer = (to_convert - 32) * 5 / 9
        self.var_feedback.set(f"Your conversion is {answer :.0f} Degrees Celsius")

    self.output_ans()


def to_fahrenheit(self):
    to_convert = self.check_input(-459)

    # gets input and converts it to the opposing temp and prints it
    if to_convert != "invalid":
        answer = (to_convert * 9 / 5) + 32
        self.var_feedback.set(f"Your conversion is {answer :.0f}{degree_sign} Degrees Fahrenheit")

    self.output_ans()