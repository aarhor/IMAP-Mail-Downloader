# IMAP Mail Downloader
This python Script downlaods all Mails from a imap Mailbox and saves them in a Folder as a `.eml` File for using them otherwise. Like an external Backup.

## Usage
Just copy / move the file `config.ini.example` to `config.ini` and fill in the needed information (values don`t need to be in "").
* `imap_server` is the imap Server (Google: `imap.gmail.com`).
  * Google: `imap.gmail.com`
  * Apple: `imap.mail.me.com`
  * Mailbox.org: `imap.mailbox.org`
  * Proton: Needs the bridge
* `imap_username` is the mailaddress or the username (r_selfhosted@example.com)
* `imap_password` can be a normal Password or an App Token.

### First run
You need the `imap-tools` python Module (`pip install imap-tools`).

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
To exclude a folder from the Backup you just need to set the full folderpath in the `folders_to_exclude` list.

## ToDo
* zip the Folder with Datestamp (`YYYYMMDD`)
* Foldername exclude not Fullpathname exclude