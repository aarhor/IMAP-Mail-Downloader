# IMAP Mail Downloader

This python Script downlaods all Mails from a imap Mailbox and saves them in a Folder as a `.zip` File for using them otherwise. Like an external Backup.<br>
This Script is tested with `Python 3.13.2` and you need the `imap-tools` python Module (`pip install imap-tools`).

## Usage

Just copy / move the file `config.ini.example` to `config.ini` and fill in the needed information (values don`t need to be in "").

- `imap_server` is, obviously, the imap Server.
  - Google: `imap.gmail.com`
  - Apple: `imap.mail.me.com`
  - Mailbox.org: `imap.mailbox.org`
  - Proton: Needs the bridge <= Not tested
- `imap_username` is the mailaddress or the username (r_selfhosted@example.com)
- `imap_password` can be a normal Password or an App Token.
- `imap_port` Default Port value `993`

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

### Configuration

| Setting               | Description                                               | Location       | default                     |
| --------------------- | --------------------------------------------------------- | -------------- | --------------------------- |
| `folders_to_exclude`  | Exclude a folder from the Backup                          | Script line 17 | `folders_to_exclude = [""]` |
| `list_Only_Folders`   | Display only folders and skips the export                 | Script line 24 | `False`                     |
| `MailBox_folder_list` | Download a specific Folder and Subfolder                  | Script line 26 | empty                       |
| `ZIP_export_folder`   | The folder for exported zip file.                         | config.ini     | `export`                    |
| `days_to_delete`      | Removes files older than x days. Disabled with value `0`. | config.ini     | `30`                        |
