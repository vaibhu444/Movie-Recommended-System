import streamlit as st
import pickle
import requests
import gzip
import zipfile



def recommend(movie_name):
    recommended_movie_names, recommended_movie_similarity = [], []
    index = movies[movies['title']==movie_name].index[0]
    similar_movies = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    for i, s in similar_movies[1:6]:
        name = movies.iloc[i].title
        recommended_movie_names.append(name)
        recommended_movie_similarity.append(s*100)
    return recommended_movie_names, recommended_movie_similarity

with zipfile.ZipFile('similarity.pkl.zip', 'r') as zipf:
    with zipf.open('similarity.pkl') as f:
        similarity = pickle.load(f)

with zipfile.ZipFile('movies_list.pkl.zip', 'r') as zipf:
    with zipf.open('movies_list.pkl') as f:
        movies = pickle.load(f)


st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_similarity = recommend(selected_movie)
    print(recommended_movie_similarity)
    for i in range(0,5):
        st.text(f"movie name: {recommended_movie_names[i]}")
    
        
