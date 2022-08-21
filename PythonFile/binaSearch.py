# Problem:
# Given a series of cards with decreasing numbers, find the position of target card

# Input: 
# cards - a list of number arranged in devreasing order
# query - a target number

# Output: the position

######################################################################
#Setp 1
# first, according to the in&output, create the signature of function
# signature is the total name of parameters
from tkinter import W


def binary_search_card(cards, query):
    pass
# name your function and think carefully about the siganature

#######################################################################
# Step 3
'''

after setting a normal eg., now consider all possible senario
1. query occurs somewhere in the middle of list(normal)
2. query is the first/last one
3. cards contains only one element, which is query
4. cards does not contain query
5. cards is empty
6. cards contains repeating numbers
7. there are more than one query in cards

these are edge cases such as empty cards or no query
if you have questions like this(edge)
1. read the questions carefully again
2. look through the examples
3. ask the interviewers for a clarification
4. make a reasonable assumption and move forward

here we return the first position when multiple positions

remember these cases are also needed to be tested
'''

#######################################################################
# Step 4
# correct solution for main situations

'''
solution 1: linear search
check the line from head to tail one by one.
Hint: discribe your algorithm makes it clear! Things above isnt
1. create a variable position with value 0
2. ckeck if number in index position equals query
3. if so, position is the answer
4. if not, position + 1 and repeat 2 - 5 until get 3
5. if number is not found, output -1 
'''

def linear_search_card(cards, query):
    pass

def linear_search_card_main(cards, query):
    # create a variab;e position with value 0
    position = 0

    # set loop and terminal conditon
    while position < len(cards):
        
        if cards[position] == query: # check if current position matches
            return position + 1 # answer

        else:
            position += 1 # keep search
        
    return position # return as error examer

def linear_search_card(cards, query):
    # error detection
    # whether cards empty
    if len(cards) == 0:
        print('Your input queue is null queue')
    else: 
        position = linear_search_card_main(cards, query)
        # if there a query in cards
        if position >= len(cards):
            return -1
        
        # output the human read position
        else: 
            return position
    

    













#######################################################################
# Step 2
'''
should be the second step
prepare some eg. to test your functions
here we use dict to set eg. and call the function to test
**dictName means passing parameters 
here it means pass 'card' = [] and 'query' = into the function
'''
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 4
}

test = {
    'input': {
        'cards': [12, 10, 4, 2, 1],
        'query': 3
    },
    'output': -1
}
# binary_search_card(**test['input']) == test['output']
# ninary_search_card(test['input']['card'], test['input']['query']) == test['output']
print(linear_search_card(**test['input']) == test['output'])

