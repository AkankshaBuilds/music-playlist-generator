# ==================================================
#              MUSIC PLAYLIST GENERATOR
# ==================================================
# This program generates a music playlist
# according to:
# 1. Language
# 2. Singer
# 3. Genre
# ==================================================

# Song Database

songs = [

    {"name": "Faded", "language": "English", "singer": "Alan Walker", "genre": "Electronic"},
    {"name": "Alone", "language": "English", "singer": "Alan Walker", "genre": "Electronic"},
    {"name": "Spectre", "language": "English", "singer": "Alan Walker", "genre": "Electronic"},
    {"name": "Darkside", "language": "English", "singer": "Alan Walker", "genre": "Electronic"},
    {"name": "On My Way", "language": "English", "singer": "Alan Walker", "genre": "Electronic"},

    {"name": "Shape of You", "language": "English", "singer": "Ed Sheeran", "genre": "Pop"},
    {"name": "Perfect", "language": "English", "singer": "Ed Sheeran", "genre": "Romantic"},

    {"name": "Believer", "language": "English", "singer": "Imagine Dragons", "genre": "Rock"},

    {"name": "Kesariya", "language": "Hindi", "singer": "Arijit Singh", "genre": "Romantic"},
    {"name": "Tum Hi Ho", "language": "Hindi", "singer": "Arijit Singh", "genre": "Sad"},
    {"name": "Apna Bana Le", "language": "Hindi", "singer": "Arijit Singh", "genre": "Romantic"},

    {"name": "Vaaste", "language": "Hindi", "singer": "Dhvani", "genre": "Pop"},

    {"name": "Brown Munde", "language": "Punjabi", "singer": "AP Dhillon", "genre": "Hip Hop"},
    {"name": "Pasoori", "language": "Punjabi", "singer": "Ali Sethi", "genre": "Fusion"}

]

# ==================================================
# Welcome Message
# ==================================================

print("=================================================")
print("           MUSIC PLAYLIST GENERATOR")
print("=================================================")

print("\nEnter Your Favorite Music Details\n")

# ==================================================
# User Input
# ==================================================

language = input("Enter Language : ")
singer = input("Enter Singer   : ")
genre = input("Enter Genre    : ")

# ==================================================
# Playlist Section
# ==================================================

print("\n=================================================")
print("                YOUR PLAYLIST")
print("=================================================\n")

song_found = False
song_number = 1

# ==================================================
# Searching Songs
# ==================================================

for song in songs:

    # Matching all conditions
    if (song["language"].lower() == language.lower() and
        song["singer"].lower() == singer.lower() and
        song["genre"].lower() == genre.lower()):

        print(song_number, ".", song["name"])

        song_number = song_number + 1

        song_found = True

# ==================================================
# If No Songs Found
# ==================================================

if song_found == False:

    print("No Matching Songs Found")
    print("Please Try Different Input")

# ==================================================
# Ending Message
# ==================================================

print("\n=================================================")
print("   THANK YOU FOR USING PLAYLIST GENERATOR")
print("=================================================")