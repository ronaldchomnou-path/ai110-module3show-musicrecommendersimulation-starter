# 🎵 Music Recommender Simulation

## Project Summary
In this project, I built a music recommender system that suggests songs based on a user’s preferences for genre, mood, and various song features such as energy, danceability, and acousticness. By using a scoring algorithm, the system ranks songs in order of relevance, providing personalized recommendations for different user profiles. This project helps understand how basic recommendation systems work and evaluates the impact of feature weightings on the recommendations.

---

## How The System Works

The recommender system works by taking a user’s preferences—such as their favorite genre, mood, and specific song features like energy and danceability—and comparing those preferences to a catalog of songs. Each song gets a score based on how well it matches the user's profile. The higher the score, the better the match.

Genre Match: If the song's genre is the same as the user’s preferred genre, it gets a big score boost (+2.0 points).
Mood Match: If the song’s mood matches the user’s mood, it gets a smaller boost (+1.0 point).
Feature Similarity: The system also compares features like energy, danceability, and acousticness to the user’s preferences. The closer the song’s feature is to the user’s target, the higher the score.

Finally, the songs are ranked and the best matches are presented as recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Changing the Genre Weight: I tested how the system behaved when I reduced the genre match weight from 2.0 to 0.5. The recommendations became more diverse but less genre-specific, making them less tailored to the user’s favorite genre.
Adding Tempo to the Score: When tempo was added as a factor in the scoring system, the recommendations became more aligned with the user's preferred energy levels. Songs with similar tempos performed better.
User Profile Variations: I tested the system with three distinct user profiles: Pop/Happiness, Lofi/Chill, and Rock/Intense. The results for each profile were consistent with my expectations, with the system prioritizing matching genres, moods, and energy levels.

---

## Limitations and Risks

Tiny Catalog: The recommender system is limited by the small catalog of songs (18 songs). Recommendations may not be diverse enough for larger-scale applications.
No Lyrics Understanding: The system does not analyze lyrics or deeper song context—only attributes like genre, mood, and energy. This limits the ability to make complex recommendations.
Genre Bias: The system can over prioritize genres like pop due to their overrepresentation in the dataset. This may lead to less diverse recommendations especially for users who prefer niche genres.

---

## Reflection

Working on this project, I learned a lot about how simple content-based recommenders can still create meaningful suggestions based on a user’s preferences. I was surprised at how quickly the system could give reasonable recommendations just by comparing numerical features like energy and danceability.

Using AI helped me quickly structure the initial code and generate the scoring logic, but I had to refine the output to ensure that the logic fit my goals. The system works well for basic recommendations, but it still has some limitations, particularly in dealing with biases that may arise from overrepresented genres.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example: VibeReader

---

## 2. Intended Use
This model is intended for educational purposes, mainly for exploring how music recommendation systems work at a fundamental level. It's not designed for real-world deployment or use in commercial platforms.

---

## 3. How It Works (Short Explanation)
This system takes a user’s profile, which includes preferences for genres, moods, and several song attributes like energy, danceability, and acousticness. Each song in the catalog is compared to these preferences and scored based on how well it matches. The scoring works as follows:

Genre Match: The song's genre is compared with the user's preferred genre. If they match, the score gets a significant boost (+2.0 points).
Mood Match: If the song’s mood aligns with the user's mood preference, it receives a smaller score boost (+1.0 point).
Feature Similarity: Attributes like energy, danceability, and acousticness are compared between the song and the user’s preferences. The closer the song’s feature is to the user’s target, the higher the score.

Each song is then ranked based on its total score, and the top-ranked songs are recommended.

---

## 4. Data
The dataset contains 18 songs.
For simplicity, no additional songs were added or removed. The dataset is kept as provided in the songs.csv file.
The dataset includes a variety of genres such as pop, rock, lofi, jazz, and more. Moods range from happy and chill to intense and melancholic.
This data is a blend of modern music genres and moods. It reflects general listener preferences but may skew toward more popular genres like pop, lofi, and rock.

---

## 5. Strengths
The system works well for users who have clear preferences for specific genres and moods. For example, users who prefer pop and happy music will receive very relevant recommendations with high scores for matching genre and mood. It provides transparency and simplicity, making it easy to explain why certain songs are recommended.
Particular user profiles it served well
Pop/Happiness profile: This profile gets accurate recommendations with clear genre and mood matches.
Lofi/Chill profile: It works effectively for users looking for a calm and relaxed vibe, where the energy and mood matching are strong.
Simplicity or transparency benefits
The simplicity of the scoring system helps in making the recommendations transparent. Each song has a clear reasoning for its score, making it easy to understand why certain songs were chosen over others.

---

## 6. Limitations and Bias
 If a user has broad or conflicting preferences (e.g., high energy and relaxed), the system may struggle to provide appropriate recommendations. Additionally, the system doesn't incorporate song lyrics or deeper context beyond attributes like genre and mood.
Does it ignore some genres or moods
Yes, because of the dataset's limitations, it may ignore less represented genres or moods (e.g., blues, classical) and favor more common ones like pop or lofi.
Does it treat all users as if they have the same taste shape
Yes, at the moment, the system assumes all users will have a consistent "shape" of preference (e.g., one favorite genre and one target mood). It doesn't yet support multiple layers of user preferences (e.g., a user who likes both rock and pop depending on the time of day).
Is it biased toward high energy or one genre by default
The model might lean more towards high-energy genres like pop and rock because they appear more frequently in the dataset. This can lead to a bias towards these genres when the user preference isn't highly specific.
How could this be unfair if used in a real product
In a real product, this model could create a "filter bubble" by recommending songs that fit a narrow scope of genres and moods, neglecting diversity in music discovery. It might unfairly prioritize popular music, ignoring niche tastes and genres.

---

## 7. Evaluation
I evaluated the system by testing it with three different user profiles: Pop/Happiness, Lofi/Chill, and Rock/Intense.

---

## 8. Future Work

If I had more time, I would: Add support for multiple user profiles, allowing for personalized recommendations for different users within the same session.
Balance the diversity of recommendations so that the system doesn’t always pick the closest match but introduces variety based on the user’s full profile.
Incorporate more features like tempo ranges, tempo variance, and lyric themes for more nuanced recommendations.

---

## 9. Personal Reflection

Building this music recommender gave me a deeper understanding of how content-based filtering works. It was interesting to see how small changes, like adjusting the weight of mood vs genre, could dramatically change the recommendations. What surprised me the most was how much human judgment still matters in the process—no algorithm can replace the emotional connection people have to music, which goes beyond just genre or energy level. For real-world use, I think a more complex model that combines both content and collaborative filtering would be beneficial. If I were to continue, I’d focus on improving the diversity of recommendations and making the system more adaptable to multiple user preferences.

