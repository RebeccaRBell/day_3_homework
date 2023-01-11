def return_10():
    return 10


def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


def length_of_string(sentence):
    return len(sentence)


def join_string(string_1, string_2):
    return string_1 + string_2


def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def number_to_full_month_name(month_number):
    return months[int(month_number - 1)]


def number_to_short_month_name(month_number):
    return months[int(month_number - 1)][:3]


def volume_of_cube(side_length):
    return side_length ** 3


def reverse_string(string):
    return string[::-1]


def fahrenheit_to_celsius(temp):
    return int(int(temp - 32) * 0.556)
