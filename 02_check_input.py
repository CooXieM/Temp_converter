def check_input(min_temp, max_temp):
    error = "Please enter a number that is more than {}".format(min_temp / max_temp)

    try:
        response = float(input("choose a number"))

        if response < min_temp:
            print(error)
        elif response > max_temp:
            print(error)

        else:
            return response

    except ValueError:
        print(error)

while True:
    check_temp = check_input(-273)
