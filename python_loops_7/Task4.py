# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# 1. Преобразуем список запрошенных ролей во множество для удаления дубликатов
unique_roles = set(requested_roles)

# 2. Находим пересечение множеств (роли, которые есть в обоих множествах)
common_roles = unique_roles & required_admin_roles

# 3. Находим недостающие административные роли (которые есть в required, но нет в unique)
missing_roles = required_admin_roles - unique_roles

# 4. Проверяем наличие роли security_officer в запросе
has_security_officer = "security_officer" in unique_roles

# Выводим результаты
print("Уникальные запрошенные роли:", unique_roles)
print("Общие административные роли:", common_roles)
print("Недостающие административные роли:", missing_roles)
print("Наличие роли security_officer в запросе:", has_security_officer)