import streamlit as st
import pickle
import requests



def recommend(movie_name):
    recommended_movie_names, recommended_movie_similarity = [], []
    index = movies[movies['title']==movie_name].index[0]
    similar_movies = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    for i, s in similar_movies[1:6]:
        name = movies.iloc[i].title
        recommended_movie_names.append(name)
        recommended_movie_similarity.append(s*100)
    return recommended_movie_names, recommended_movie_similarity
        


st.header('Movie Recommender System')

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

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
    
        