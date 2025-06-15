import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
# from pysteamauth.auth import Steam
import streamlit as st
# import streamlit_authenticator as stauth
# Création du menu qui va afficher les choix qui se trouvent dans la variable options

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
selection = option_menu(
    menu_title=None,
    options=["Accueil", "Photos", "Info"],
    icons=["house", "camera", "info-circle"],  # Ajout d'icônes
    default_index=0  # Définit l'option par défaut
)
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
elif selection == "info":
    st.write("Our info") 
# ... et ainsi de suite pour les autres pages



# Création de 3 colonnes 
col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

# Contenu de la troisième colonne : 
with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")
  
  
# Création de deux colonnes où col2 est deux fois plus large que col1 :
col1, col2 = st.columns([1, 2])


# On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", # Question affichée
    ("Email", "Home phone", "Mobile phone") # Options proposées
)
customer_input = st.sidebar.text_input("Enter your response here:")
# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    add_radio = st.radio(
        "Choose a shipping method",  # Titre de la question
        ("Standard (5-15 days)", "Express (2-5 days)")  # Choix proposés
    )
  

