
def clean_items(items):
    cleaned = []
    for item in items:
        item = item.strip()
        # Пропускаем: пустые строки ИЛИ одиночные запятые
        if not item or (item == ',' and not cleaned):
            continue
        # Если предыдущий элемент заканчивается на запятую (например, "Применение,"), объединяем
        if cleaned and cleaned[-1].endswith(','):
            cleaned[-1] = f"{cleaned[-1]} {item}"
        else:
            cleaned.append(item)
    return cleaned