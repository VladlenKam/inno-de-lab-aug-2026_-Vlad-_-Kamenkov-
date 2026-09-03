# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Извлекаем значения host и port из вложенного словаря connection
host = db_config["connection"]["host"]
port = db_config["connection"]["port"]

# Безопасно проверяем наличие ключа ssl_settings и вложенного параметра ssl_mode
# Если ключа нет, используем значение по умолчанию "verify-full"
ssl_mode = db_config["connection"].get("ssl_settings", {}).get("ssl_mode", "verify-full")

# Изменяем пользователя на "admin"
db_config["connection"]["user"] = "admin"

# Добавляем новый параметр max_connections со значением 100
db_config["connection"]["max_connections"] = 100

# Выводим обновленное содержимое конфигурации
print("SSL Mode:", ssl_mode)
print("Параметры соединения:")
for key, value in db_config["connection"].items():
    print(f"* {key}: {value}")