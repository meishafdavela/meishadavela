def make_album(artist, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album
 
 
album_1 = make_album('wave to earth', 'love')
album_2 = make_album('ariana grande', 'love me harder', songs=12)
album_3 = make_album('the weeknd', 'out of time', songs=12)
album_4 = make_album('taylor swift', '1989', songs=13)
 
print(album_1)
print(album_2)
print(album_3)
print(album_4)