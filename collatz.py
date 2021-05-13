def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

while True: # REMEMBER BREAK STATEMENTS TO GET OUT OF WHILE TRUE LOOPS
    try:
        n = int(input('Enter a number:'))
        break
    except ValueError:
        print('Enter an integer!')

while n != 1:
    n = collatz(n)
