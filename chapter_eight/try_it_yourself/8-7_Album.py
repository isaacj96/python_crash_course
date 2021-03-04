def make_album(artist, album, songs = None):        
    group = {'name': artist, 'album_name': album}
    if songs:
        group['Number of sogs'] = songs
    return group

album_one = make_album('Tame Impala', 'Lonerism')
album_two = make_album('Frank Ocean', 'Blonde')
album_three = make_album('Lana Del Rey', 'Lust for Life')
album_four = make_album('Mac Demarco', 'Salad Days', 8)
print(album_one)
print(album_two)
print(album_three)
print(album_four)
