import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9c4243acb7b010d18630b63d06be9a82'.format(movie_id))
    data = response.json()
    # print(data['poster_path'].dtype)
    return "http://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    
    recommended_movies = []
    recommended_moviePoster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch Poster
        recommended_moviePoster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_moviePoster

st.title('FilmFusion')

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
    'Search the movie',movies['title'])

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    
    col1, col2, col3 = st.columns(3)
   
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(posters[3])
        st.text(names[3])
    with col2:
        st.image(posters[4])
        st.text(names[4])
    with col3:
        st.image(posters[5])
        st.text(names[5])
