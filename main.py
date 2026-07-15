#from lp import LP
from lp_collection import LPCollection
from playlist import RandomPlaylist
#from playlist import Playlist
from controls import Controls
from settings import Settings


if __name__ == '__main__':
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