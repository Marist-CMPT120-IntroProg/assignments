def calculate_average(xs):
    '''Add up the numbers in a list and divide by its length'''
    # Variables allow us to keep track of data of hold value for later
    total = 0
    # Loops allow us to repeat instructions
    for i in range(len(xs)): # Python initializes i to 0, then counts 1 at a time, up to but including 6
        # add the next number from the list into the total
        total += xs[i]
    avg = total / len(xs)
    return avg

def read_numbers():
    '''Read a sequence of integers from the keyboard'''
    xs = []
    keep_running = True
    while keep_running is True: # here, keep_running is a (continuation) test expression
        user_input = input("Enter a number, or Q to quit: ")
        if user_input == "Q":
            keep_running = False
        else:
            next_number = int(user_input)
            xs.append(next_number)
    return xs

def read_numbers_into(xs):
    '''Read a sequence of integers from the keyboard into an existing list'''
    keep_running = True
    while keep_running is True: # here, keep_running is a (continuation) test expression
        user_input = input("Enter a number, or Q to quit: ")
        if user_input == "Q":
            keep_running = False
        else:
            next_number = int(user_input)
            xs.append(next_number)

def main():
    numbers = read_numbers()
    print(f"The average of the user's numbers is {calculate_average(numbers)}.\n")

    more_numbers = [ 20, 10, 15, 30, 100 ]
    print(f"The average of the computer's numbers is {calculate_average(more_numbers)}.\n")

    read_numbers_into(more_numbers)
    print(f"The average of a mix of numbers is {calculate_average(more_numbers)}.\n")

main()
