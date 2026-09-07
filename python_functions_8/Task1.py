MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Рассчитывает стоимость партии аренды фильмов и проверяет превышение лимита.

    Args:
        quantity (int): Количество дисков в партии.
        rental_rate (float): Стоимость аренды одного диска.
        discount (float, optional): Размер скидки. По умолчанию 0.0.

    Returns:
        tuple[float, bool]: Общая сумма (с округлением до 2 знаков) и флаг превышения лимита.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

# Тестовые данные
test_data = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 0.1),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.50, 0.2),
]

print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===")
for name, qty, rate, disc in test_data:
    total, exceeded = calculate_rental_batch(qty, rate, disc)
    print(f"Партия {name}: Сумма {total}$. Превышение лимита: {exceeded}")