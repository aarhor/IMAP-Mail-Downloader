from imap_tools import MailBox
from contextlib import redirect_stdout
import os

folders_to_exclude = [""]
imap_server = ""
imap_username = ""
imap_password = ""  # Normal Password or an App-Token
list_Only_Folders = False

with MailBox(imap_server).login(imap_username, imap_password) as MailBox:
    for g in MailBox.folder.list():
        Ordner = g.name
        
        if Ordner not in folders_to_exclude:
            print(Ordner)
            if not list_Only_Folders:
                if not os.path.exists(f"{imap_server}/{Ordner}"):
                    os.makedirs(f"{imap_server}/{Ordner}")

                MailBox.folder.set(Ordner)
                for msg in MailBox.fetch(mark_seen=False):
                    uid = msg.uid
                    invalid_char = [
                        ":",
                        "“",
                        "\r\n",
                        "„",
                        '"',
                        "!",
                        "?",
                        "/",
                        "\\",
                        "*",
                        "<",
                        ">",
                        "|",
                        "ß",
                        "\t",
                        "\r",
                        "\n",
                    ]
                    
                    titel = msg.subject
                    for zeichen in invalid_char:
                        titel = titel.replace(zeichen, "_")

                    DateiPfad = f"{imap_server}/{Ordner}/{uid}_{titel}.eml"
                    
                    if not os.path.exists(DateiPfad):
                        raw_email = msg.obj
                        print(DateiPfad)
                        with open(DateiPfad, "w", encoding="utf-8") as g:
                            with redirect_stdout(g):
                                print(raw_email)
