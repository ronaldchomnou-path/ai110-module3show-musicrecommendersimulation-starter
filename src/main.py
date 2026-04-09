from recommender import load_songs, recommend_songs

# ----------------------------
# User Profiles
# ----------------------------
default_profile = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "target_valence": 0.8,
    "target_danceability": 0.7,
    "target_acousticness": 0.2
}

chill_lofi_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.4,
    "target_valence": 0.6,
    "target_danceability": 0.6,
    "target_acousticness": 0.7
}

intense_rock_profile = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.9,
    "target_valence": 0.5,
    "target_danceability": 0.2,
    "target_acousticness": 0.1
}

def main():
    songs = load_songs("data/songs.csv")
    
    for profile in [default_profile, chill_lofi_profile, intense_rock_profile]:
        top_songs = recommend_songs(profile, songs, k=5)
        print(f"\n--- Top recommendations for {profile['favorite_genre'].title()} / {profile['favorite_mood'].title()} ---")
        for idx, song in enumerate(top_songs, start=1):
            print(f"{idx}. {song['title']} by {song['artist']} - Score: {song['score']:.2f}")
            print("   Reasons:", ", ".join(song["reasons"]))

if __name__ == "__main__":
    main()