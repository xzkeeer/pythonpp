def calculate(expression):
    try:
        if "+" in expression:
            a, b = expression.split("+")
            return float(a) + float(b)

        elif "-" in expression:
            a, b = expression.split("-")
            return float(a) - float(b)

        elif "*" in expression:
            a, b = expression.split("*")
            return float(a) * float(b)

        elif "/" in expression:
            a, b = expression.split("/")
            b = float(b)
            if b == 0:
                return "Ошибка: деление на ноль"
            return float(a) / b

        elif "%" in expression:
            a, b = expression.split("%")
            b = float(b)
            if b == 0:
                return "Ошибка: деление на ноль"
            return float(a) % b

        else:
            return "Неизвестная операция"

    except ValueError:
        return "Ошибка: неверный формат ввода"


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
