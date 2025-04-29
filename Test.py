import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lire le token secret depuis secrets.toml
EXPECTED_TOKEN = st.secrets["access"]["token"]

# Lire le token depuis l'URL
query_params = st.experimental_get_query_params()

provided_token = query_params.get("token", [""])[0]

if provided_token != EXPECTED_TOKEN:
    st.error("Accès refusé : token invalide ou manquant.")
    st.stop()

st.title("📊 Visualisation des ventes mensuelles")

# Exemple de données
data = {
    "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
    "Ventes": [120, 150, 100, 170, 200, 130]
}
df = pd.DataFrame(data)

# Affichage du tableau
st.write("Voici les données de ventes :")
st.dataframe(df)

# Affichage du graphique
fig, ax = plt.subplots()
ax.plot(df["Mois"], df["Ventes"], marker='o')
ax.set_title("Évolution des ventes")
ax.set_ylabel("Ventes")
st.pyplot(fig)
