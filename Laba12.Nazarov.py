import random

def get_user_choice():
    while True:
        user_choice = input("Выберите камень (r), ножницы (s) или бумагу (p): ").lower()
        if user_choice in ['r', 's', 'p']:
            return user_choice
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

def get_computer_choice():
    choices = ['r', 's', 'p']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        return "Вы победили!"
    elif user_choice == computer_choice:
        return "Ничья!"
    else:
        return "Компьютер победил!"

def main():
    print("Добро пожаловать в игру 'Камень - ножницы - бумага'!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == '__main__':
    main()