def calculate(expression):

    allowed_chars = "0123456789+-*/%.()"

    for char in expression:
        if char not in allowed_chars:
            return "Ошибка: недопустимый символ"
 
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result

    except ZeroDivisionError:
        return "Ошибка: деление на ноль"

    except Exception:
        return "Ошибка: неверный формат выражения"


def main():
    print("Простой калькулятор")
    print("Примеры ввода: 2+2, 10/5, 7%3")
    print("Для выхода введите 'exit'")

    while True:
        user_input = input("\nВведите выражение: ").replace(" ", "")

        if user_input == "exit":
            print("Выход из программы")
            break

        result = calculate(user_input)
        print("Результат:", result)


if __name__ == "__main__":
    main()
