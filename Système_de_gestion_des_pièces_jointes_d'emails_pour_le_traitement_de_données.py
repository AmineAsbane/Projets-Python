import imaplib
import email
from email.header import decode_header
import os
import pandas as pd
from dotenv import load_dotenv

# Charger les variables d'environnement (email, mot de passe)
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Connexion à la boîte email via IMAP
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(EMAIL, PASSWORD)
imap.select("inbox")

# Rechercher les mails non lus avec pièces jointes
status, messages = imap.search(None, '(UNSEEN)')
mail_ids = messages[0].split()

# Dossier de téléchargement
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Parcourir les mails
for mail_id in mail_ids:
    status, msg_data = imap.fetch(mail_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject = decode_header(msg["subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            print(f" Mail: {subject}")

            # Traiter les pièces jointes
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                filename = part.get_filename()
                if filename and filename.endswith(".csv"):
                    filepath = os.path.join("downloads", filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    print(f" Pièce jointe téléchargée : {filename}")

                    # Nettoyage du fichier
                    df = pd.read_csv(filepath)
                    df.drop_duplicates(inplace=True)
                    df.dropna(how='all', inplace=True)
                    df.to_csv(f"downloads/cleaned_{filename}", index=False)
                    print(f" Fichier nettoyé : cleaned_{filename}")

# Fermer la connexion
imap.logout()
