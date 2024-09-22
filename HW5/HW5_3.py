#Создайте функцию генератор чисел Фибоначчи

def fibona_generator(n=None):
    a, b = 0, 1
    count = 0

    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1


fibo_gen = fibona_generator(20)
print(list(fibo_gen))