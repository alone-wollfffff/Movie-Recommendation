import streamlit as st
import pickle
import pandas as pd

# 1. Load the saved data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Recommendation function logic from your notebook
def recommend(movie_title):
    try:
        # Find index of the movie
        index = movies[movies['title'] == movie_title].index[0]
        # Get similarity scores
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movies = []
        # Get top 5 recommendations (excluding the movie itself)
        for i in distances[1:6]:
            recommended_movies.append(movies.iloc[i[0]].title)
        return recommended_movies
    except:
        return ["Movie not found in database."]

# 3. Streamlit UI
st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'Search or select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write("Movies you might also like:")
    for i in recommendations:
        st.success(i)