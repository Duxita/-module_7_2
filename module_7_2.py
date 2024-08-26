def custom_write(file_name, strings):
    strings_position = {}
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(f'{string}\n')
            strings_position[(len(strings_position) +1, position)] = string
        return strings_position
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)




