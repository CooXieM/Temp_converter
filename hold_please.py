def to_celsius(self):
    to_convert = self.check_input(-273)

    if to_convert != "error":
        # Calculations
        self.var_feedback.set(f"Converting {to_convert} to *F")
        return to_convert


def to_fahrenheit(self):
    to_convert = self.check_input(-459)

    if to_convert != "error":
        self.var_feedback.set(f"Converting {to_convert} to *C")
        return to_convert


command = self.to_fahrenheit
command = self.to_celsius