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
