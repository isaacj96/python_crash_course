def make_album(artist, album, songs=None):
    group = {'name': artist, 'album_name': album}
    if songs:
        group['Number of songs'] = songs
    return group


while True:
    print("\nPlease enter the Artist name")
    print("(enter 'q' at any time to quit)")

    f_artist = input("Name: ")
    if f_artist == 'q':
        break
    album_name = input("Name of Album: ")
    if album_name == 'q':
        break
    number_of_songs = input("Please enter number of songs: ")
    if number_of_songs == 'q':
        break
    else:
        number_of_songs = int(number_of_songs)

    create_album = make_album(f_artist, album_name, number_of_songs)
    print(f"\n{create_album}")
