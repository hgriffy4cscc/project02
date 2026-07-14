#from lp import LP
from lp_collection import LPCollection
#from playlist import Playlist
from controls import Controls
from settings import Settings


if __name__ == '__main__':
    settings = Settings()
    controls = Controls(settings)
    lp_collection = LPCollection(settings)
    lp_collection.get_the_data()
    controls.do_menu_and_response()
    lp_collection.search_lpcollection(controls)