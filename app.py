import streamlit as st
import pandas as pd
import pickle
import requests


movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')

# def recommend(movie):
#
#
#     movie_ind = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_ind]
#     movies_list5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     list5 = []
#     for i in movies_list5:
#         list5.append(movies.iloc[i[0]].title)
#     return list5
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=c4aa2d551f6e0d2b9cb7ce145687591b&language=en-US'.format(movie_id))
    data = response.json()

    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']




def recommend( movie ):
    movie_ind = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_ind]
    movies_list5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6] #index and similarity score
    list5 = []
    imgpath =[]
    for i in movies_list5:
        list5.append(movies.iloc[i[0]].title)
        imgpath.append(fetch_poster(movies.iloc[i[0]].id))
    return list5,imgpath


sel_movie = st.selectbox(
    'Enter a movie name',
    movies['title'].values)

st.write('You selected:', sel_movie)


if st.button('Recommend'):
    img_title,img_path = recommend(sel_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(img_title[0])
        st.image(img_path[0])

    with col2:
        st.text(img_title[1])
        st.image(img_path[1])

    with col3:
        st.text(img_title[2])
        st.image(img_path[2])

    with col4:
        st.text(img_title[3])
        st.image(img_path[3])
    with col5:
        st.text(img_title[4])
        st.image(img_path[4])