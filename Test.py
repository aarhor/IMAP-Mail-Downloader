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
        Foldername = g.name

        if Foldername not in folders_to_exclude:
            print(Foldername)
            if not list_Only_Folders:
                if not os.path.exists(f"{imap_server}/{Foldername}"):
                    os.makedirs(f"{imap_server}/{Foldername}")

                MailBox.folder.set(Foldername)
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

                    Mail_Subject = msg.subject
                    for char in invalid_char:
                        Mail_Subject = Mail_Subject.replace(char, "_")

                    FilePath = f"{imap_server}/{Foldername}/{uid}_{Mail_Subject}.eml"

                    if not os.path.exists(FilePath):
                        raw_email = msg.obj
                        print(FilePath)
                        with open(FilePath, "w", encoding="utf-8") as g:
                            with redirect_stdout(g):
                                print(raw_email)
