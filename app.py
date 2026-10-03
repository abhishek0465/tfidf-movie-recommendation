import streamlit as st
import pickle
import joblib
import numpy as np
import time

st.title('Movie Recommendation System')

similarity_score = joblib.load('similarity_score.joblib')
with open('movies_data.pkl','rb') as file:
    movie_data = pickle.load(file)

def reset_recommendations():
    st.session_state.show_recommendations = False

movie_select = st.selectbox("Select a Movie!",movie_data,on_change=reset_recommendations)
number_of_movies = st.slider("Chose Numnber of Movies to Recommend:",2,8,2)

def recommend(movie_name, top_n=5):
    index = movie_data[movie_data['title']==movie_name].index[0]
    scores = similarity_score[index]
    similar_movies = sorted(enumerate(scores),reverse=True,key=lambda x:x[1])[1:top_n+1]
    recommendaed_movies = []
    for i in similar_movies:
        recommendaed_movies.append(movie_data.iloc[i[0]].title)
    return recommendaed_movies

if 'show_recommendations' not in st.session_state:
    st.session_state.show_recommendations = False

if st.button("Recommend Movies"):
    st.session_state.show_recommendations = True

if st.session_state.show_recommendations:
    recomendations = recommend(movie_select,number_of_movies)
    for i in recomendations:
        st.write(i)
        time.sleep(0.1)