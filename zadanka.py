import numpy as np
import random


# ## elements bigger than list
# list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_length = len(list)
# list_2 = []
# for x in range (0,list_length):
#     if list[x] > 10:
#         list_2.append(list[x])
#
# print(list_2)
#
# print([aa for aa in list if aa<5])
#
# ## Divisors
# number = input("give a number: ")
# number = int(number)
# divisors=[]
# for i in range (1,number+1):
#     if number % i == 0:
#         divisors.append(i)
#
# print(divisors)
#
# # elements from two lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(a + [x for x in b if not x in a])
# print(set(a) & set(b))
# print(set(a) | set(b))
#
# word = input("ask if it's a palindrome: ")
# reverse = word[::-1]
# print(["it's a palindrome" if word == reverse else "it's not a palindrome"])
#
# # list less than ten ## im high
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# print([aa for aa in a if aa<5])
#
# print("\n next line")
#
# new = []
# for item in a:
#     if (item<5):
#         new.append(item)
# print(new)
#
# print('\n')
#
# print(list(filter(lambda x:)))
#
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([aa for aa in a if aa % 2 == 0])
#
# # rock papers
# while True:
#
#     first_bet = input('player one make a bet: ')
#     second_bet = input('player 2 make a bet: ')
#
#     if first_bet == second_bet:
#         print('a draw')
#     elif first_bet == 'rock' and second_bet == 'paper':
#         print('player 2 wins')
#     elif first_bet == 'rock' and second_bet == 'scissors':
#         print('player 1 wins')
#
#     play_again = input(' \n play again Y/N?')
#     if play_again == "N \n":
#         break
#
# # guessing number game
#
# random = np.random.randint(1,10)
# print(random)
#
# while True:
#     guess = input('guess a number: ')
#     guess = int(guess)
#     if guess == random:
#         print('lucky')
#         break
#     elif guess < random:
#         print('za mao')
#     elif guess > random:
#         print('too much')
#
## prime check
# a = 1
# number = input('check for primes: ')
# number = int(number)
# for divisor in range (a,number):
#     if number % divisor == 0:
#         a += a
# print('its a prime' if a<3 else 'not a prime')
#
##password generator
# string = 'abcdefghijklmnoprstuvwqABCDEFGHIJKLMNOPRSTQUW1234567890123456789'
# password = ''
# length = input('how long should the password be: ')
# length = int(length)
# for letter in range (length) :
#     password = password + random.choice(string)
#
# print(password)
#
#
## web page decode







