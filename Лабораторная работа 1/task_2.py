#disk_v = 1.44  - мб
disk_v = 1.44 * 1024 * 1024  #перевод в байты
count_pages = 100
count_lines = 50
count_symb = 25
one_symb_v = 4  #байта

books_v = one_symb_v * count_symb * count_lines * count_pages  #одной книги

count_books = disk_v // books_v

print("Количество книг, помещающихся на дискету:", round(count_books))
