# FILE NAME - coin_toss.py

# NAME: Casey Tatar
# DATE: 3/1/2026
# BRIEF DESCRIPTION:  This program is a simple application that will randomly return Heads or Tails. To calculate, a random number between 1 and 100 (inclusive) is generated and if the number is 51 or greater then Tails is reported. Otherwise Heads is reported.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!

import random

def main():
    coinflipper()

def coinflipper():

    headsortails = random.randint(1, 100) 

    print('===== Coin Flipper =====')
    
    if headsortails >= 51: 
        print('Tails')

    else: print('Heads')

main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

The hardest part of completing this lab was remembering how to use random numbers. 





'''
