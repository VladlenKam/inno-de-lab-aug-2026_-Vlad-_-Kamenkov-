# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# Разбиваем строку на части по разделителю ';'
parts = raw_user_record.split(';')
# Очищаем каждый элемент от лишних пробелов с помощью генератора списка
clean_parts = [part.strip() for part in parts]
# Добавляем префикс UID- к первому элементу (идентификатор пользователя)
user_id = f"UID-{clean_parts[0]}"
# Заменяем подчёркивание на пробел во втором элементе (имя пользователя)
temp = clean_parts[1].replace('_', ' ')
# Преобразуем имя в формат "Каждое Слово С Заглавной Буквы"
user_name = temp.title()
# Приводим третий элемент (город) к верхнему регистру
city_name = clean_parts[2].upper()
# Приводим четвёртый элемент (статус) к нижнему регистру
user_status = clean_parts[3].lower()
# Собираем все обработанные элементы в список
final_parts = [user_id, user_name, city_name, user_status]
# Объединяем элементы в одну строку с разделителем " | "
result = " | ".join(final_parts)
# Выводим результат
print(result)