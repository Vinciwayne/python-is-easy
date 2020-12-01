"""
Lollipop is the first single from American rapper Lil Wayne's sixth studio album, Tha Carter III.
The track posthumously features American singer Static Major and is produced by Deezle and Jim Jonsin.
It heavily utilizes the Auto-Tune vocal effect. The song was released digitally on March 13, 2008.


"""


"""
on this python code i used
strings 
integers
decimals(floats)


"""




# dictionary = lolipop_track
lollipop_track = {
    'artist':'lil wayne, Static Major',
    'music_title':'lollipop', 
    'year_released':2008,
    'recorded':2007, 
    'genre':'Electropop, R&B dirty, rap',
    'Duration':'4 min 30 sec',
    'producers':'Deezle, Jim Jonsin',
    'record_labels':'Cash Money, Universal Motown', 'song_writers':'Dwayne Carter, Stephen, Garrett, Darius Harrison, Jim Jonsin, Rex Zamor, Marcus Cooper',
    'artist_net_worth':151000000
            }
for x, y in lollipop_track.items():
        print(x + " : " + str(y))

print()
print()



# function = guesstrackinfo
def guesstrackinfo(x, y):
    return x in lollipop_track and lollipop_track[x] == y

print("Is the title of this song \"lollipop\"?: {}".format(
   guesstrackinfo("music_title", "lollipop")))
print()
print()
print("was is released in \"2008\"?: {}".format(
    guesstrackinfo("year_released", 2008)))








"""


EZEBUIRO
UCHECHUKWU 
VINCENT 


"""