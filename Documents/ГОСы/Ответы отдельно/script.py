import docx
import os

def extract_tickets(input_file):
    # Проверяем, что файл существует
    if not os.path.exists(input_file):
        print(f"Файл {input_file} не найден!")
        return
    
    # Загружаем документ
    doc = docx.Document(input_file)
    
    # Собираем весь текст документа
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    # Объединяем все параграфы в одну строку для удобства обработки
    text = "\n".join(full_text)
    
    # Разделяем текст по меткам "X Билет"
    tickets = []
    current_pos = 0
    
    for i in range(1, 26):
        start_marker = f"{i} Билет"
        end_marker = f"{i+1} Билет" if i < 25 else None
        
        # Находим начало текущего билета
        start_pos = text.find(start_marker, current_pos)
        if start_pos == -1:
            print(f"Маркер '{start_marker}' не найден!")
            continue
        
        # Находим начало следующего билета (конец текущего)
        if end_marker:
            end_pos = text.find(end_marker, start_pos)
            if end_pos == -1:
                print(f"Маркер '{end_marker}' не найден!")
                continue
            ticket_content = text[start_pos + len(start_marker):end_pos].strip()
        else:
            ticket_content = text[start_pos + len(start_marker):].strip()
        
        tickets.append((start_marker, ticket_content))
        current_pos = start_pos + len(start_marker)
    
    # Сохраняем каждый билет в отдельный файл
    for ticket in tickets:
        filename = f"{ticket[0]}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ticket[1])
        print(f"Создан файл: {filename}")

if __name__ == "__main__":
    input_filename = "Ответы.docx"
    extract_tickets(input_filename)