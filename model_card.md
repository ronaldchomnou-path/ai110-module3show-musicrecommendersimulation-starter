# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

TuneMatch 

---A

## 2. Intended Use  

This model is designed to generate personalized music recommendations based on a user's preferred genre, mood, and specific song features like energy, valence, and danceability. It takes a "taste profile" from the user and compares it to a catalog of songs to produce a ranked list of song recommendations.

Assumptions:
The model assumes the user has specific preferences (e.g., favorite genre, mood, energy level) that can be used to rank songs.
It works best for simple music recommendation scenarios based on these parameters (genre, mood, energy, etc.).
This model is intended for classroom exploration and learning. It is not meant for real-world users or commercial deployment at this time. 

---

## 3. How the Model Works  

The model works by scoring songs based on how well they match a user's profile. The profile includes the user's favorite genre, mood, and their preferences for various song attributes like energy, valence, and acousticness.

Song Features: The model uses features such as genre, mood, energy, danceability, and acousticness to calculate a score for each song.
User Preferences: The user's preferences (favorite genre, mood, energy target, etc.) are compared against the song attributes to determine how closely each song matches the user’s profile.
Scoring: The scoring logic works by adding points when a song’s genre or mood matches the user’s preferences. Additionally, for numerical features like energy, danceability, and acousticness, the song is given points based on how close its value is to the user's target. The closer the song's features are to the user's preferences, the higher the score.

---

## 4. Data  

The dataset contains 18 songs.
The catalog includes various genres such as pop, lofi, rock, jazz, blues, and more.
Moods like "happy," "chill," "intense," and others are represented, but the dataset could benefit from more diverse mood categories.
No songs were removed, but I added additional songs in the dataset to ensure a variety of genres and moods.
The dataset doesn’t include more complex aspects like lyrics or user behavior data, which are crucial for advanced recommenders like Spotify or TikTok. 

---

## 5. Strengths  

The system works well for users who have clear preferences for genres or moods (e.g., "Pop / Happy" or "Rock / Intense").
The scoring system effectively captures matching genres and moods, producing reasonable recommendations for users with those preferences.
For users who enjoy a particular genre or mood, the recommendations generally align with expected results. For instance, the "Lofi / Chill" profile tends to recommend calm, mellow tracks, which fits well with the user's preferences. 

---

## 6. Limitations and Bias 

The system does not take into account other potentially valuable features like lyrics, user behavior, or advanced musical attributes (e.g., tempo).
Genre Bias: The system tends to prioritize genre matching more than mood or energy. If a user has a specific genre preference, the recommendations can become skewed toward songs from that genre, potentially overlooking good matches in terms of mood or other features.
Limited Dataset: The relatively small catalog size of 18 songs means the system may not perform well with a broader or more diverse set of songs. It also means the model might over-recommend certain genres (e.g., pop, lofi).
No Contextual Understanding: The system does not consider factors like the user's recent listening history or personal context (e.g., time of day, activity). These factors could affect the relevance of the recommendations.

---

## 7. Evaluation  

The system was evaluated by testing three distinct user profiles: Pop / Happy, Lofi / Chill, and Rock / Intense. I checked whether the top recommendations matched the expected genre and mood preferences.

Expected Results: The recommendations were consistent with the users’ preferences. For example, the "Pop / Happy" profile received upbeat pop songs, while the "Rock / Intense" profile received high-energy rock tracks.
Surprises: It was interesting to see how closely the energy and mood features influenced the results, often more than genre alone. However, sometimes songs from similar genres but mismatched moods ranked lower than expected.

---

## 8. Future Work  

To improve recommendations, I could add features like tempo or song popularity, which would add more depth to the scoring process.
I would like to extend the system to support multiple users with distinct preferences. This could involve handling multiple taste profiles at once.

---

## 9. Personal Reflection  

This project gave me a deeper understanding of how simple music recommendation systems work. I was surprised by how much weight genre matching has in determining the top recommendations, and how even a small change in feature importance can affect the output.

Building this system made me realize how powerful simple algorithms can be in simulating real world music recommenders. However there is still room for human judgment in the recommendation process, especially when it comes to adding personal context and handling more complex user preferences. 
