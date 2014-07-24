#Написать функцию, которая будет проверять, что введённая пользователем строка действительно является числом в интервале [a;b]
#И если это не так, то будет просить пользователя повторить попытку ввода.

def input_int(a, b):
    usr_number = input("Please, enter a number between {} and {}\n".format(a, b))
    while True:
        if usr_number.isdigit() and a <= int(usr_number) <= b : # Проверяем, что пользователь ввел именно число и в задданых рамках.
            break
        else:
            usr_number = input("You wrong. It's simple. You just need to enter a number between {} and {}\n".format(a, b))
    return usr_number
