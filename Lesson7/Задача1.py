message_for_user_1 = 'Введите стихотворение: '

poem = input(message_for_user_1).split(' ')
result = list(map(lambda poem: poem.count('а'), poem))

if sum(result) / len(result) == result[0]:
    print('Парам пам-пам')
else:
    print('Пам парам')