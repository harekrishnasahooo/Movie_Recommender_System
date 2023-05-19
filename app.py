import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4b425a3dd34297af9a0712f84a14c8dd".format(movie_id))
    data= response.json()
    #st.text(data)
    poster_path=data['poster_path']
    return "https://image.tmdb.org/t/p/w300/" + poster_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies=[]
    recommend_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommend_movies,recommend_movies_poster




movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recomendation')

selected_movie_name = st.selectbox(
    'How would you like to be connnected?',
    movies['title'].values )

if st.button("Recommend"):
    names,poster=recommend(selected_movie_name)

    tab1, tab2, tab3 ,tab4, tab5= st.tabs([names[0], names[1], names[2],names[3],names[4]])

    with tab1:
        st.header(names[0])
        st.image(poster[0])

    with tab2:
        st.header(names[1])
        st.image(poster[1])

    with tab3:
        st.header(names[2])
        st.image(poster[2])
    with tab4:
        st.header(names[3])
        st.image(poster[3])
    with tab5:
        st.header(names[4])
        st.image(poster[4])