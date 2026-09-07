import time

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

def performance_logger(func):
    """
    Декоратор для логирования времени выполнения функции.

    Args:
        func (Callable): Оборачиваемая функция.

    Returns:
        Callable: Функция-обёртка с логированием времени.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = round(end - start, TIME_DECIMALS)
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {duration} сек.")
        return result
    return wrapper

@performance_logger
def get_sorted_report(data: list) -> list:
    """
    Сортирует список категорий по выручке.

    Args:
        data (list[dict[str, str | float]]): Список словарей с ключами category и total_sales.

    Returns:
        list[dict[str, str | float]]: Отсортированный список по убыванию выручки.
    """
    return sorted(data, key=lambda x: x["total_sales"], reverse=True)

test_sets = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ],
    [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ],
    [
        {"category": "Drama", "total_sales": 500.00}
    ]
]

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
for idx, test_data in enumerate(test_sets, start=1):
    print(f"\n--- ТЕСТ {idx} ---")
    sorted_data = get_sorted_report(test_data)
    print("Топ категорий по выручке:")
    for i, item in enumerate(sorted_data, start=1):
        print(f"{i}. {item['category']}: {item['total_sales']}")