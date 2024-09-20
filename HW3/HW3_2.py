# В большой текстовой строке подсчитать количество встречаемых слов 
# и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

jack_house = (
    "Вот дом Который построил Джек "
    "А это пшеница Которая в темном чулане хранится "
    "В доме Который построил Джек "
    "А это веселая птица синица "
    "Которая часто ворует пшеницу "
    "Которая в темном чулане хранится "
    "В доме Который построил Джек "
)

words = [word.lower().strip(".?!:;,") for word in jack_house.split()]

word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print("10 самых часто встречающихся слов:")
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")