import random as r

alphabet1 = []
alphabet2 = []

letters1 = (
        'а', 'е', 'и', 'о',
        'у', 'й', 'э', 'ы',
        'ю', 'я'
)
letters2 = (
        'б', 'в', 'г', 'д', 'ж', 'з',
        'к', 'л', 'м', 'н', 'п', 'р',
        'с', 'т', 'ф', 'х', 'ш', 'щ',
        'ч', 'ц', 'ъ', 'ь'
)
# creating random list of letters
while len(alphabet1) < 6:
    index = r.randint(1, len(letters1)) - 1
    if letters1[index] not in alphabet1:
        alphabet1.append(letters1[index])
    else:
        continue

while len(alphabet2) < 9:
    index = r.randint(1, len(letters2)) - 1
    if letters2[index] not in alphabet2:
        alphabet2.append(letters2[index])
    else:
        continue
alphabet = alphabet1 + alphabet2
list.sort(alphabet)
print(alphabet)

user1_score = 0

user2_score = 0

username1 = input('Введите имя первого игрока: ')

username2 = input('Введите имя второго игрока: ')

user1words = []

user2words = []

value = input('До скольки очков играем?: ')

score_value = int(value)


def sravnenie1():
    global word1
    global user1_score
    global user1words
    global user2words
    ind = 0
    while ind <= (lenword - 1):
        if word1[ind] in alphabet:
            ind += 1

        else:
            return print('Таких букв нет в списке! ' + username1 + ', Не жульничай! \nПереход хода!')

    word1 = ''.join(word1)

    if word1 not in user1words and word1 not in user2words:
        print('Ваше слово: ' + str(word1) + ', вы заработали ' + str(len(word1)) + ' очков')
    else:
        return print('Такое слово уже было! ' + username1 + ', Не жульничай! \nПереход хода!')
    user1words.append(word1)
    user1_score += len(word1)


def sravnenie2():
    global word2
    global user2_score
    global user2words
    global user1words
    ind = 0
    while ind <= (lenword2 - 1):
        if word2[ind] in alphabet:
            ind += 1

        else:
            return print('Таких букв нет в списке! ' + username2 + ', Не жульничай! \nПереход хода!')

    word2 = ''.join(word2)

    if word2 not in user1words and word2 not in user2words:

        print('Ваше слово: ' + str(word2) + ', вы заработали ' + str(len(word2)) + ' очков')
    else:
        return print('Такое слово уже было! ' + username2 + ', Не жульничай! \nПереход хода!')
    user2words.append(word2)
    user2_score += len(word2)


def winner():
    if score_value <= user1_score > user2_score:

        print('Игрок ' + username1 + ' победил, набрав ' + str(user1_score) + ' очков!')
        print('Слова, использованные игроком', username1, ':', user1words)

    elif score_value <= user2_score > user1_score:

        print('Игрок ' + username2 + ' победил, набрав ' + str(user2_score) + ' очков!')
        print('Слова, использованные игроком', username2, ':', user2words)

    else:
        print('Победила дружба!!! У нас одинаковое количество очков, мы с тобой оба умные, аж спасу нет!))')
        print('Слова, которые были использованы игроком', username1, ':', user1words)
        print('Слова, которые были использованы игроком', username2, ':', user2words)


while user1_score < score_value > user2_score:

    print(username1 + ' ходит: ')
    print(alphabet)
    word1 = input('Составьте слово из этих букв: ')
    lenword = len(word1)
    word1 = list(word1)

    sravnenie1()

    print('Всего очков у игрока ' + username1 + ' : ' + str(user1_score))

    print(username2 + ' совершает ход: ')
    print(alphabet)
    word2 = input('Составьте слово из этих букв: ')
    lenword2 = len(word2)
    word2 = list(word2)

    sravnenie2()

    print('Всего очков у игрока ' + username2 + ' : ' + str(user2_score))

    if user1_score >= score_value or user2_score >= score_value:
        winner()
