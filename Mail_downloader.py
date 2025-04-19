from imap_tools import MailBox
import datetime
from contextlib import redirect_stdout
import os
import configparser
import zipfile

Path_config = "config.ini"
config = configparser.ConfigParser()
config.sections()
config.read(Path_config)
config.sections()
"imap" in config

folders_to_exclude = [""]
imap_server = config["imap"]["imap_server"]
imap_username = config["imap"]["imap_username"]
imap_password = config["imap"]["imap_password"]
imap_port = config["imap"]["imap_port"]
list_Only_Folders = False
date = datetime.datetime.now().strftime("%Y%m%d")
MailBox_folder_list = ""
ZIP_export_folder = f"export"

with MailBox(imap_server, port=imap_port).login(
    imap_username, imap_password
) as MailBox:
    for g in MailBox.folder.list(MailBox_folder_list):
        Foldername = g.name

        if Foldername not in folders_to_exclude:
            print(Foldername)

            if not list_Only_Folders:
                if not os.path.exists(f"export/{imap_server}/{Foldername}"):
                    os.makedirs(f"export/{imap_server}/{Foldername}")

                with open(
                    f"export/{imap_server}/Structure.txt", "a", encoding="utf-8"
                ) as g:
                    with redirect_stdout(g):
                        print(Foldername)

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

                    FilePath = (
                        f"export/{imap_server}/{Foldername}/{uid}_{Mail_Subject}.eml"
                    )

                    if not os.path.exists(FilePath):
                        raw_email = msg.obj
                        print(FilePath)
                        with open(FilePath, "w", encoding="utf-8") as g:
                            with redirect_stdout(g):
                                print(raw_email)


def zipfolder(foldername, target_dir):
    zipobj = zipfile.ZipFile(
        f"{ZIP_export_folder}/{foldername}.zip", "w", zipfile.ZIP_DEFLATED
    )
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])


zipfolder(f"{imap_server}_{date}", f"export/{imap_server}")
