'''
* @Author: Samarth BM.
* @Date: 2021-09-08 20:48  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-08 20:59
* @Title: Flip Coin and print percentage of Heads and Tails
'''

import random

num_of_toss = int(input("Enter the number of times you want to flip the coin "))
tail = 0
head = 0

for toss in range(num_of_toss):
    toss = random.random() # To generate random numbers from 0.0 to 1.0
    if toss < 0.5:
        print("Tails")
        tail += 1
    else:
        print("Heads")
        head += 1

# Calculating the percentage of tails and heads.
tail_percent = (tail*100)/num_of_toss
head_percent = (head*100)/num_of_toss

print("Tail percentage is ",tail_percent, " and head percentage is ",head_percent)

