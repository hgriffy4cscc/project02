"""griffy_project02_main.py

Project 2: (more emphasis on portfolio presentation->architectural justification);
any project that demos concepts from 8-11, ideally by refactoring and building on Project 1

    functions - done
    object-oriented (classes) - done (a few ways)
    file i/o - done
    exception handling - done (somewhat)
    data persistence - done
    automated testing - not yet done

This project demonstrates basic python concepts and practices by providing
an interactive search and display program for a collection of vinyl records.
Specifically, it demonstrates object-oriented programming.
Additional functionality include:
* creating a random collection of lps
* saving that randomized playlist to file

Resources:
    * course materials (obvi)
    * way to assign arbitrary attributes based on dictionary addapted from:
        https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python
    * reading csv code/advice from https://www.geeksforgeeks.org/python/working-csv-files-python/
    * avoid pylint error for unused variable in a for loop just needed for count (replace with _):
        https://stackoverflow.com/questions/52792987/unused-variable-in-a-for-loop
    * simulate input() for pytest:
        https://www.pythontutorials.net/blog/how-to-test-a-function-with-input-call/

Todo:
    * Testing
"""
from lp_collection import LPCollection
from playlist import RandomPlaylist
from controls import Controls
from settings import Settings

def do_the_thing():
    settings = Settings()
    controls = Controls(settings)
    lp_collection = LPCollection(settings)
    lp_collection.get_the_data()
    keep_playing = True
    while keep_playing:
        controls.do_menu_and_response()
        if controls.do_what == 'q':
            print('Thank you for playing!')
            keep_playing = False
        elif controls.do_what in 'at':
            lp_collection.search_lpcollection(controls)
            lp_collection.output_results()
        elif controls.do_what == 'r':
            playlist = RandomPlaylist(settings, lp_collection)
            playlist.build_random_playlist(controls)
            playlist.output_results()
            if controls.ask_to_save_file():
                playlist.save_results_to_file(controls)

if __name__ == '__main__':
    do_the_thing()
