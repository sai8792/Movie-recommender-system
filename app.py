import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity = pickle.load(open('similsrity.pkl', 'rb'))

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")

option = st.selectbox(
    "select a movie",
   options = movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

