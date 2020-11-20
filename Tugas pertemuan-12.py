import os
word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return word[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
            return terbilang(n // 1_000) + " thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
            return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n // 10 == 2:
            return 'twenty ' + (terbilang(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 3:
            return 'thirty ' + (terbilang(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 5:
            return 'fifty ' + (terbilang(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 4:
            return 'forty ' + (terbilang(n % 10) if n % 10 != 0 else '')
        else:
            return terbilang(n // 10) + 'ty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    else:
        if n == 10:
            return 'ten'
        elif n == 11:
            return 'eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        else:
            return terbilang(n % 10) + 'teen'        

while True:
    os.system('cls')
    try:
        n = int(input('Imput Your Number : '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('Your input is Wrong !! ')
    os.system('pause')