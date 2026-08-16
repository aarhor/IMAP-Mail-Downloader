# IMAP Mail Downloader

**🦅🦅ENGLISH VERSION BELOW🦅🦅**

Dieses python Skript lädt alle Mails von einem IMAP E-Mail Postfach herunter und speichert diese in einer `.zip` Datei. Die Datei kann dann z.B. für ein externes Backup genutzt werden.<br>
Getestet wurde das Skript mit `Python 3.13.2`. 
Folgende Module werden zusätzlich bennötigt:
* `imap-tools` => `pip install imap-tools`, `sudo apt install python3-imap-tools`
* `pyzipper` => `pip install pyzipper`, `sudo apt install python3-pyzipper`

## Nutzung

Damit das Skript sich mit dem gewünschten IMAP Server verbinden kann, erstelle eine Kopie der Datei `config.ini.example` (Befindet sich im Ordner `config`) und benne sie um in `config.ini`. Anschließend trage die benötigten Informationen in die Konfigurationsdatei ein. Falls weitere Postfächer gesichert werden sollen, erstelle nach belieben weitere Kopien der Beispieldatei. Wenn beim Starten der Parameter `--config_file=[Name der config Datei]` mit angegeben wird, wird das entsprchende Postfach über die angegeben Daten gesichert.

- `imap_server` ist der imap Server.
  - Google: `imap.gmail.com`
  - Apple: `imap.mail.me.com`
  - Mailbox.org: `imap.mailbox.org`
  - Proton: Benötigt [die bridge](https://proton.me/de/mail/bridge)<br>
    ^ Erfolgreich mit einer SSL Verbindung getestet. Das Skript kann, ohne weitere Einstellungen, mit einer SSL Verbindung genutzt werden. STARTTLS wird nicht unterstützt.
  - ...
- `imap_username` ist die Mailadresse oder der Benutzername (r_deEDV@example.com)
- `imap_password` kann ein normales Passwort sein oder ein App Token.
- `imap_port` Der Port. Standardmäßig `993`
- `days_to_delete` Wie viele Tage an Backups behalten werden soll.
- `encryption_password` Das Kennwort zum verschlüsseln des Exports. Es **muss** ein Kennwort angegeben werden.

### Erste Durchführung

Für die erste Ausführung empfehle ich die Variable `list_Only_Folders` auf `True` zu setzen, um die "wahren" und kompletten Ordnernamen / Pfade zu erhalten.<br>
Falls später ein Ordner ausgeschlossen werden soll, muss dieser exakt so geschrieben werden wie dieser in der Ausgabe angegeben ist.

Die Ausgabe sollte in etwa so aussehen:

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

### Variablen

| Einstellung           | Beschreibung                                                   | Zeile im Skript | Standardwert                |
| --------------------- | -------------------------------------------------------------- | --------------- | --------------------------- |
| `folders_to_exclude`  | Schließt einen Ordner von der Sicherung aus.                   | Zeile 17        | `folders_to_exclude = [""]` |
| `list_Only_Folders`   | Zeigt nur alle Ordner an und führt keine Sicherung aus.        | Zeile 24        | `False`                     |
| `MailBox_folder_list` | Sichert nur einen spzifischen Ordner / Unterordner             | Zeile 26        |                             |
| `ZIP_export_folder`   | Wo die `.zip` Datei gespeichert werden soll.                   | config.ini      | `export`                    |
| `days_to_delete`      | Löscht alle Sicherungen älter als x Tage. Deaktiviert mit `0`. | config.ini      | `30`                        |

### Parameter

| Einstellung      | Beschreibung                                      | Standardwert |
| ---------------- | ------------------------------------------------- | ------------ |
| `--config_file=` | Gibt die config Datei an die genutzt werden soll. | `config.ini` |

#### --config_file=

Beispiel: `--config_file=config_gmail.ini`<br>
Gibt an welche config Datei für die Sicherung genutzt werden soll. Der Name der Datei kann frei gewählt werden, jedoch **muss** diese sich in dem Unterordner `config` befinden. Wenn nichts angegeben wird, wird Standardmäßig die Datei `config.ini` genutzt.

---

<br>

This python Script downlaods all Mails from a imap Mailbox and saves them in a Folder as a `.zip` File for using them otherwise. Like an external Backup.<br>
This Script is tested with `Python 3.13.2` and you need the `imap-tools` python Module (`pip install imap-tools`).

## Usage

Just copy / move the file `config.ini.example` (can be found in the folder `config`) to `config.ini` and fill in the needed information (values don`t need to be in ""). When you need to backup more than one Mailbox, just copy the example file and fill in the needed Information for the Mailbox.

- `imap_server` is, obviously, the imap Server.
  - Google: `imap.gmail.com`
  - Apple: `imap.mail.me.com`
  - Mailbox.org: `imap.mailbox.org`
  - Proton: Needs [the bridge](https://proton.me/de/mail/bridge)<br>
    ^ Successfully tested with an IMAP **SSL** Connection. The Script can be used as it is with an SSL Connection. But not usable with an STARTTLS Connection.
  - ...
- `imap_username` is the mailaddress or the username (r_selfhosted@example.com)
- `imap_password` can be a normal Password or an App Token.
- `imap_port` Default Port value `993`
- `days_to_delete` For how long a backup should be kept.
- `encryption_password` The password to encrypt the export. You **have to** set a password to use the script. 

### First run

For the first run I recommend to set the Variable `list_Only_Folders` to `True`, to get the "real" and full foldernames / paths.<br>
If you want to exclude an folder, you have to use the full name.

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

### Parameter

| Setting          | Description           | default      |
| ---------------- | --------------------- | ------------ |
| `--config_file=` | Sets the config file. | `config.ini` |

#### --config_file=

Example: `--config_file=config_gmail.ini`<br>
Specifies which config file should be used for the backup. The file name can be freely chosen, but it **must** be located in the `config` subfolder. If nothing is specified, the `config.ini` file is used by default.
