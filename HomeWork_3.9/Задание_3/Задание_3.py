text_list = ['1.txt', '2.txt', '3.txt']

text_read = {}

for text in text_list:
    with open(text, 'rt', encoding='utf8' ) as text_print:
        text_read[text] = text_print.read()

for text_el in text_read.values():
    quantity = 0
    if text_el == "\n":
    # Найти команду для \n
        quantity += 1
    print(quantity)

# разобраться с упорядовачинием словаря
# разобраться с выводом