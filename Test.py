import streamlit as st
import pandas as pd

# Saisie du mot de passe
password = st.text_input("Mot de passe", type="password")

if password == "monmotdepasse":
    st.success("Accès autorisé")
    # Ton application ici
else:
    st.warning("Mot de passe requis pour accéder à l'application")
    st.stop()

# Titre principal
st.title("Capacités Production : Analyse et Comparaison")

# Description ou options globales si nécessaire
st.write("Bienvenue dans l'outil d'analyse des capacités de production.")
st.write("Utilisez le menu de gauche pour naviguer entre les fonctionnalités disponibles.")
