import pickle
import streamlit as st
import requests
import pandas as pd



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:6]:
        movie_id = movies.iloc[i[0]].movie_id
        if i==distances[0]:
            most_related_movie=movies.iloc[i[0]].title
            most_related_movie_poster=fetch_poster(movie_id)
            continue

        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return most_related_movie,most_related_movie_poster, recommended_movie_names, recommended_movie_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')


page = st.sidebar.radio("Navigation",['Home','About'],index=0)

if page == 'Home':

    selected_movie_name=st.selectbox("Search Your Movie", movies['title'].values)

    if st.button('Recommend'):
        mrm,mrmp,recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
        
        st.header("Your Movie")
        mcol1, mcol2, mcol3 = st.columns(3)
        with mcol1:
            st.write(mrm)
            st.image(mrmp)

        st.header("Related Movies")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.write(recommended_movie_names[0])
            
        with col2:
            st.image(recommended_movie_posters[1])
            st.write(recommended_movie_names[1])
            
        with col3:
            st.image(recommended_movie_posters[2])
            st.write(recommended_movie_names[2])
            
        with col4:
            st.image(recommended_movie_posters[3])
            st.write(recommended_movie_names[3])
            
        with col5:
            st.image(recommended_movie_posters[4])
            st.write(recommended_movie_names[4])

if page == "About":
    st.subheader('''Content Based Reccomendation of Movies''')
    st.text('A list of 5000 movies are choosen from TMDb dataset\nSearch for any movie and get reccomendations of similar movies\n(Please note that the movies are used from an old dataset)')
    dataset = 'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'
    sourcecode = 'https://github.com/suhas-0812/Movie-Recommendation---Content-Based-Filtering'
    st.markdown(f'<a href={sourcecode}><button style="background-color:grey;display: block; width: 100%">Source - Code </button></a>', unsafe_allow_html=True)
    st.markdown(f'<a href={dataset}><button style="background-color:grey;display: block; width: 100%">Dataset used</button></a>', unsafe_allow_html=True)
    st.subheader("Contact:")
    st.text("SUHAS R")
    first , last = st.columns(2)
    first1 , last1 = st.columns(2)
    
    linkedin = 'https://www.linkedin.com/in/suhas-r-b92aaa228/'
    github = 'https://github.com/suhas-0812'
    whatsapp = 'https://wa.me/918277013148'
    
    first.markdown(f'<a href={linkedin}><button style="background-color:grey;display: block; width: 100%">Linked In</button></a>', unsafe_allow_html=True)
    last.markdown(f'<a href={github}><button style="background-color:grey;display: block; width: 100%">Github</button></a>', unsafe_allow_html=True)
    first1.markdown(f'<button style="background-color:grey;display: block; width: 100%">Email - suhasrsagar0812@gmail.com</button>', unsafe_allow_html=True)
    last1.markdown(f'<a href={whatsapp}><button style="background-color:grey;display: block; width: 100%">Whatsapp</button></a>', unsafe_allow_html=True)  
