from imap_tools import MailBox
import datetime
from contextlib import redirect_stdout
import os
import sys
import configparser
import shutil
import time
import pyzipper

Path_config = ""
script_path = os.path.dirname(__file__)

if len(sys.argv) >= 2:
    Arg_SingleDB = sys.argv[1]
    Path_config = f"{script_path}/config/{Arg_SingleDB.replace("--config_file=", "")}"
else:
    Path_config = f"{script_path}/config/config.ini"

config = configparser.ConfigParser(interpolation=None)
config.sections()
config.read(Path_config)
config.sections()
"config" in config

folders_to_exclude = [""]
imap_server = config["config"]["imap_server"]
imap_username = config["config"]["imap_username"]
imap_password = config["config"]["imap_password"]
imap_port = config["config"]["imap_port"]
encryption_password = config["config"]["encryption_password"]
ZIP_export_folder = config["config"]["zip_export_folder"]
days_to_delete = int(config["config"]["days_to_delete"]) * 24 * 60 * 60
list_Only_Folders = False
date = datetime.datetime.now().strftime("%Y%m%d")
MailBox_folder_list = ""
now = time.time()
errorcounter = 0


def zipfolder(foldername):
    if errorcounter >= 1:
        foldername = f"{foldername}_haserrors"

    zip_path = f"{ZIP_export_folder}/{foldername}.zip"
    source_path = f"export/{imap_server}/"

    if not os.path.exists(source_path):
        print(f"Hinweis: Ordner {source_path} existiert nicht.")
        return

    with pyzipper.AESZipFile(zip_path, "w", compression=pyzipper.ZIP_DEFLATED) as zf:
        zf.setpassword(encryption_password.encode("utf-8"))  # Set Encryption password
        zf.setencryption(pyzipper.WZ_AES)  # Set Encryption

        for root, dirs, files in os.walk(source_path):
            for file in files:
                full_path = os.path.join(root, file)

                rel_path = os.path.relpath(full_path, source_path)
                zf.write(full_path, arcname=rel_path)


with MailBox(imap_server, port=imap_port).login_utf8(
    imap_username, imap_password
) as MailBox:
    for g in MailBox.folder.list(MailBox_folder_list):
        Foldername = g.name

        if Foldername not in folders_to_exclude:
            print(Foldername)

            if not list_Only_Folders:
                try:
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

                        filename = f"{uid}_{Mail_Subject}"

                        if len(filename) > 250:
                            filename = f"{filename[:250]}"

                        FilePath = f"export/{imap_server}/{Foldername}/{filename}.eml"

                        if not os.path.exists(FilePath):
                            raw_email = msg.obj
                            print(FilePath)
                            with open(FilePath, "w", encoding="utf-8") as g:
                                with redirect_stdout(g):
                                    print(raw_email)
                except Exception as error:
                    with open(
                        f"export/{imap_server}/Error.log", "a", encoding="utf-8"
                    ) as g:
                        with redirect_stdout(g):
                            print(
                                f"An exception occurred:\n{error}\n\nGoing to the next Iteration.\n"
                                "--------------------------------------------------------"
                            )
                    errorcounter += 1
                    continue

if not list_Only_Folders:
    zipfolder(f"{imap_server}_{date}", f"export/{imap_server}")
    shutil.rmtree(f"export/{imap_server}")

    if days_to_delete > 0:
        for filename in os.listdir(ZIP_export_folder):
            filepath = os.path.join(ZIP_export_folder, filename)

            if os.path.isfile(filepath):
                creation_time = os.path.getmtime(filepath)

                if (now - creation_time) > days_to_delete:
                    os.remove(filepath)
