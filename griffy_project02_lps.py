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

###### READ DATA FROM CSV ######
def get_the_data(filename: str = 'lps.csv'):
    """
    Extract data from a csv file and return it for processing

    Args:
        filename: optional Name of csv file to get data from.

    Returns:
        get_lps: a list of dictionaries with all csv data
        get_fields: a list of field names
    """
    get_fields = []  # Column names
    get_lps = []    # Data rows
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)  # Reader object

        get_fields = next(csvreader)  # Read header
        for row in csvreader:     # Read rows
            get_lps.append(row)
    return get_fields, get_lps

    #print("Total no. of rows: %d" % csvreader.line_num)  # Row count

    #for row in titles[:5]:
    #    print(row)

###### PROMPT USER AND GATHER INPUT ######
def menu_and_response():
    """
    Prompt user for input and return that input in variables

    Returns:
        do_what: which action the user wants to take
        for_what: search string to use when searching
        how_many: maximum number of lps to return (or 0 for all)
    """
    get_do_what, get_for_what, get_how_many = "", "", 0
    is_get_do_what_valid = False
    while not is_get_do_what_valid:
        get_do_what: str = input("What would you like to do? q to quit, "
                                 "a to search by artist, t to search by title: ").lower()
        if len(get_do_what) == 1 and get_do_what in 'qat':
            is_get_do_what_valid = True
    if get_do_what != 'q': #if user quitting, don't prompt for additional input
        is_get_for_what_valid = False
        while not is_get_for_what_valid:
            get_for_what: str = input("Enter text to search for: ")
            if get_for_what:
                is_get_for_what_valid = True
        get_how_many = input("How many results would you like? (zero to display all): ")
        # integer-checking code adapted from
        # https://www.geeksforgeeks.org/python/check-if-string-is-integer-in-python/
        try:
            get_how_many = int(get_how_many)
        except ValueError:
            get_how_many = len(lps)
    return get_do_what, get_for_what, get_how_many

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
