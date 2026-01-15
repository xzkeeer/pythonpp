import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def calculate(expression: str) -> str | float:
    """
    Вычисляет математическое выражение.
    :return: результат вычисления или сообщение об ошибке
    """
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


def main() -> None:
    """
    Точка входа в программу.
    Запускает цикл ввода выражений.
    """
    logging.info("Простой калькулятор")
    logging.info("Примеры ввода: 2+2, 10/5, 7%3")
    logging.info("Для выхода введите 'exit'")

    while True:
        user_input: str = input("\nВведите выражение: ").replace(" ", "")

        if user_input == "exit":
            logging.info("Выход из программы")
            break

        result = calculate(user_input)
        logging.info(f"Результат: {result}")


if __name__ == "__main__":
    main()
