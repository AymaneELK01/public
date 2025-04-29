import streamlit as st
import pandas as pd

# Lire un secret simple
token = st.secrets["token_secret"]
st.write("Le token secret est :", token)

# Lire un secret dans une section
username = st.secrets["database"]["username"]
password = st.secrets["database"]["password"]

st.write("Nom d'utilisateur de la base de données :", username)


# Titre principal
st.title("Capacités Production : Analyse et Comparaison")

# Description ou options globales si nécessaire
st.write("Bienvenue dans l'outil d'analyse des capacités de production.")
st.write("Utilisez le menu de gauche pour naviguer entre les fonctionnalités disponibles.")
