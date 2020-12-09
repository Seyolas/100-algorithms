#2 farklı cümledeki ortak kelimeleri bulma  "2 kümenin kesişimi"
sentence1="We are really pleased to meet you In our city"
sentence2="the city was hit By a really heavy storm "

def fonksiyon(kelime1,kelime2):
        set1 = set(sentence1.split())
        set2 = set(sentence2.split())

        return list(set1&set2)


print(fonksiyon(sentence1,sentence2))