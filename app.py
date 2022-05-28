import pickle
import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="NextFlim",
    page_icon='🎥',
    layout="wide",
    initial_sidebar_state="expanded"
)


def get_poster(movie_id):
    data = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=c9db491236361f8e67d70cad9df2eff5&language=en-US".format(
            movie_id))
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommendations(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    vector_distance = similarity[movie_idx]
    recommended_movies = sorted(list(enumerate(vector_distance)), reverse=True, key=lambda x: x[1])[1:6]

    mlist = []
    mposter = []
    for j in recommended_movies:
        movie_id = movies.iloc[j[0]].id
        mlist.append(movies.iloc[j[0]].title)
        mposter.append(get_poster(movie_id))
    return mlist, mposter


moviesDict = pickle.load(open('movie_dict.pkl', 'rb'))
movieInfo = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(moviesDict)
movie_db = pd.DataFrame(movieInfo)

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Search'):
    col1, col2 = st.columns(2)
    idx = movie_db.index[movie_db['title'] == selected_movie].tolist()
    mid = movie_db.iloc[idx[0]].id
    movie_pic = get_poster(mid)

    with col1:
        st.header(selected_movie)
        st.image(movie_pic)

    with col2:
        st.subheader('Overview:')
        st.write(movie_db.iloc[idx[0]].overview)
        st.subheader('Genre:')
        st.write(movie_db.iloc[idx[0]].genres)
        st.subheader('Cast:')
        st.write(movie_db.iloc[idx[0]].cast)
        st.subheader('Director:')
        st.write(movie_db.iloc[idx[0]].crew)

    with st.sidebar:
        st.subheader('Recommended:')
        r_name, r_poster = recommendations(selected_movie)

        for i in range(5):
            st.image(r_poster[i])
            st.text(r_name[i])
