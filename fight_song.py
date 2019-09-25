
"""
Printing out the lyrics of a song using helper functions.

Author: Oğuzhan Çölkesen
"""

def song_couplet():
    print("Go, team go!")
    print("We can do it.")
    
def song_body():
    song_couplet()
    print("We're the 'cats,")
    print("We'll leave it at that.")
    song_couplet()

def fight_song():
    """
    Prints out the lyrics to an admittedly uninspiring Wildcats fight song.
    """
    song_couplet()
    print()
    song_body()
    print()
    song_body()
    print()
    song_couplet()
    
fight_song()