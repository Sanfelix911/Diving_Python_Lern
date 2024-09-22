#Напишите однострочный генератор словаря, 
# который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и 
# суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

def premium_calculation(names, rates, premiums):
    return {
        name: rate * (float(premium.strip("%")) / 100)
        for name, rate, premium in zip(names, rates, premiums)
    }


n = ['Alex', 'Ben', 'Mio']
b = [20000, 10000, 30000]
r = ['5.5%', '10.25%', '3.14%']

print(premium_calculation(n, b, r))