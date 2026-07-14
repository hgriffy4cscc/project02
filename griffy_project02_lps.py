"""griffy_project02.py

Project 2: (more emphasis on portfolio presentation->architectural justification); any project that demos concepts from 8-11, ideally by refactoring and building on Project 1

    functions
    object-oriented (classes)
    file i/o
    exception handling
    data persistence
    automated testing

This project demonstrates basic python concepts and practices by providing
an interactive search and display program for a collection of vinyl records.
Specifically, it demonstrates object-oriented programming.
Additional functionality include:
* creating a playlist of albums
* selecting 1+ random collection of objects

Resources:
    * csv code/advice from https://www.geeksforgeeks.org/python/working-csv-files-python/

Todo:
    * Develop a random results function to return some random set of lps
"""
#import random
import csv

matching_indexes = []



###### FIND MATCHING LPS ######
def search_lps() -> list[int]:
    """
    Return up to maximum number of lps where title matches the given search string.

    Args:
        none but uses the folling variables from outer scope(s)
        lps: list of dictionaries for dataset
        search_field: the field to be searched
        for_what: the search string provided by user
        how_many: maximum number of matches to return

    Returns:
        matching_indexes: list of indexes for matching dictionary items in lps list
    """
    for i, lp in enumerate(lps):
        # h/t https://www.geeksforgeeks.org/python/enumerate-in-python/
        if for_what.lower() in lp[search_field].lower():
            matching_indexes.append(i)
    return matching_indexes[:how_many]

###### OUTPUT RESULTING MATCHES ######
def output_results():
    """
    Outputs matched lps items

    Args:
        none, but uses the following variables from outer scope(s)
        matching_indexes: indexes for lps that match search
        fields: the list of fields in the dataset
        lps: dictionary of the dataset

    Side-effect:
        output to the terminal
    """
    #print(f"Responses were: {do_what} :: {for_what} :: {how_many}")
    #print(f"Matching indexes: {matching_indexes}")
    for i in matching_indexes:
        print(f"{'_'*80}")
        for f in fields:
            print(f"{f}: {lps[i][f]}")

###### MAIN BLOCK OF CODE ######
#start the ball rolling by getting the data
fields, lps = get_the_data()

#involve the user by asking what they want to do the first time
do_what, for_what, how_many = menu_and_response()

#define a flag to know when to quit (when user says quit)
keep_going: bool = True

#loop to keep searching as long as the user wants to play
while keep_going:

    if do_what == 'q': # special loop for quitting program
        print("Thanks for playing. Have an amazing day!")
        keep_going = False
    elif do_what == 'a' or do_what == 't':
        #define search field
        if do_what == 'a':
            search_field: str = 'who'
        elif do_what == 't':
            search_field: str = 'what'
        matching_indexes: list[int] = [] #reset results to empty list
        matching_indexes = search_lps()
        output_results()
        do_what, for_what, how_many = menu_and_response()
    else:
        print("Not sure how to interpret your reply. Please enter data as prompted")
        do_what, for_what, how_many = menu_and_response()
