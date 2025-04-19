# IMAP Mail Downloader
This python Script downlaods all Mails from a imap Mailbox and saves them in a Folder as a `.eml` File for using them otherwise. Like an external Backup.<br>
This Script is tested with `Python 3.13.2` and you need the `imap-tools` python Module (`pip install imap-tools`).

## Usage
Just copy / move the file `config.ini.example` to `config.ini` and fill in the needed information (values don`t need to be in "").
* `imap_server` is, obviously, the imap Server.
  * Google: `imap.gmail.com`
  * Apple: `imap.mail.me.com`
  * Mailbox.org: `imap.mailbox.org`
  * Proton: Needs the bridge
* `imap_username` is the mailaddress or the username (r_selfhosted@example.com)
* `imap_password` can be a normal Password or an App Token.
* `imap_port` Default Port value `993`

### First run
For the first run I recommend to set the Variable `list_Only_Folders` to `True`, to get the "real" and full foldernames / paths.

The export should look something like this:
```plaintext
Archiv
Junk
Trash
Drafts
Sent
INBOX/CatchAll
INBOX/Kino
INBOX/Amazon
INBOX/Selfhosted
INBOX/Selfhosted/NAS
INBOX/Selfhosted/Paperless
INBOX
```
To exclude a folder from the Backup you just need to set the full folderpath in the `folders_to_exclude` list. When you excluded some folders, just set the Variable `list_Only_Folders` back to `False` and start the script with `py Mail_downloader.py`.

If you just want to Download a specific Folder and Subfolder, set `MailBox_folder_list` to the Foldername. For example: `MailBox_folder_list = "INBOX/Selfhosted"`.

To set a another export folder for the zip File than the default `export`, just Update `ZIP_export_folder`.