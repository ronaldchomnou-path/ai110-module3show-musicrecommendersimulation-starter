import csv

def load_songs(filepath):
    songs = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numeric fields
            for key in ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]:
                row[key] = float(row[key])
            songs.append(row)
    return songs

def score_song(user_profile, song):
    score = 0
    reasons = []

    if song["genre"].lower() == user_profile["favorite_genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_profile["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    for feature in ["energy", "valence", "danceability", "acousticness"]:
        diff = abs(song[feature] - user_profile[f"target_{feature}"])
        feature_score = max(0, 1 - diff)  # closer = higher
        score += feature_score
        reasons.append(f"{feature} similarity (+{feature_score:.2f})")

    return score, reasons

def recommend_songs(user_profile, songs, k=5):
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_profile, song)
        scored_song = song.copy()
        scored_song["score"] = score
        scored_song["reasons"] = reasons
        scored_songs.append(scored_song)

    # Sort by score descending
    scored_songs.sort(key=lambda x: x["score"], reverse=True)
    return scored_songs[:k]