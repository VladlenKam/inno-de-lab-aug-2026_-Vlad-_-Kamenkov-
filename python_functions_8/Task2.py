DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(film_name: str, days_overdue, fine_rate: float) -> tuple[float, float]:
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        print(f"Фильм: '{film_name}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index
    except TypeError:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_name}': {days_overdue}")
    except ValueError:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_name}': {days_overdue}")
    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_name}': float division by zero")
    finally:
        print("--- Проверка транзакции возврата завершена ---\n")

# Тесты
print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
test_cases = [
    ("Matrix", 5, 1.5),
    ("Inception", "пять", 2.0),
    ("Avatar", 0, 2.5),
    ("Interstellar", [3], 3.0)
]

for film, days, rate in test_cases:
    calculate_overdue_fine(film, days, rate)