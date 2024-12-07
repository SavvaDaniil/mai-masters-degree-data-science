

def read_data_txt_and_print_lines_only_with_numbers() -> None:
    """Чтение содержимое текстового файла 'data.txt' и печать содержащиеся в нем только тех строк, которые содержат числовые значения"""
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line == '\n':
                    continue
                try:
                    int(line)
                except ValueError:
                    raise TypeError(f'Строка {line} не является числом')
                print(str(int(line)))
    except FileNotFoundError as e:
        print(f'Error FileNotFoundError: {e}')
    except TypeError as e:
        print(f'Error TypeError: {e}')

if __name__ == '__main__':
    read_data_txt_and_print_lines_only_with_numbers()