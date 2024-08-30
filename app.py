'''import streamlit as st
import pickle
import pandas as pd

from streamlit import title
def recommend(movie):
    movie_index = movie[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.loads(open('movie_dict.pkl','rb').read())
movies = pd.DataFrame(movies_dict)

similarity = pickle.loads(open('similarity.pkl','rb').read())

st.title("Movie Recmmender System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

#st.button("Reset", type="primary")
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)
'''

import streamlit as st
import pickle
import pandas as pd


def recommend(movie_name):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie_name].index[0]

    # Get the similarity scores for this movie
    distances = similarity[movie_index]

    # Get the top 5 most similar movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Prepare the list of recommended movie titles
    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]

        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load the movies dictionary and similarity matrix
movies_dict = pickle.loads(open('movie_dict.pkl', 'rb').read())
movies = pd.DataFrame(movies_dict)
similarity = pickle.loads(open('similarity.pkl', 'rb').read())

# Streamlit application title
st.title("Movie Recommender System")

# Movie selection dropdown
selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

# Recommendation button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
