text = "пара-ра-рам рам-пам-папам па-ра-па-да"

words = text.split()

print(words)

if all(list(map(lambda x: x.count('а') == words[0].count('а'), words))):
    print("Парам пам-пам")
else:
    print("Пам парам")
