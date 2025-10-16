import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
data = {
    'Title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Batman Begins',
        'Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets',
        'The Lord of the Rings', 'The Hobbit', 'The Avengers'
    ],
    'Description': [
        'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.',
        'A thief who steals corporate secrets through the use of dream-sharing technology.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'When the menace known as the Joker emerges, Batman must accept one of the greatest psychological tests.',
        'After training with his mentor, Batman begins his fight to free crime-ridden Gotham City.',
        'An orphaned boy enrolls in a school of wizardry and learns about his destiny.',
        'Harry returns for his second year at Hogwarts School of Witchcraft and Wizardry.',
        'A meek Hobbit from the Shire sets out to destroy the One Ring.',
        'Bilbo Baggins is swept into a quest to reclaim a treasure from the dragon Smaug.',
        'Earth\'s mightiest heroes must come together and learn to fight as a team.'
    ]
}


df = pd.DataFrame(data)


vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Description'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_movie(title, cosine_sim=cosine_sim):
    
    idx = df[df['Title'].str.lower() == title.lower()].index[0]

    
    sim_scores = list(enumerate(cosine_sim[idx]))

    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]
print("Movies similar to 'Inception':")
print(recommend_movie("Inception"))

print("\nMovies similar to 'Harry Potter and the Sorcerer\'s Stone':")
print(recommend_movie("Harry Potter and the Sorcerer's Stone"))