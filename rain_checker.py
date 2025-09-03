import time
import requests
from bs4 import BeautifulSoup
import os

# URL de la page Clash.gg
URL = "https://clash.gg/"
# On récupère l’URL depuis les variables d’environnement Render
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
# Ton webhook Discord
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1412796910074462280/kxF8smM5FAz6n-ktANWNjPdTB3IQ8dWYKPS1jVbwK_QJoyI1pLazdVkTd3Q5cow3ULX9"

def check_rain_pool():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Cherche le bouton avec le texte Join / Joined
    button = soup.find("button")
    if button and "Join" in button.text:
        send_discord("🔥 Le Rain Pool est dispo ! Va vite claim sur Clash.gg 🔗")
    else:
        print("Pas encore dispo...")

def send_discord(message):
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

# Boucle infinie
while True:
    try:
        check_rain_pool()
    except Exception as e:
        print("Erreur :", e)

    time.sleep(300)  # check toutes les 5 minutes
