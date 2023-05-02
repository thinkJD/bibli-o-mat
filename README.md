# bibli-o-mat 🤖

Mit den Kindern sind wir ständig in der Bücherei. Wenn die ausgeliehenen Medien fällig werden bekommt man eine Mail und hat dann 2 Tage Zeit die Medien zurückzugeben oder zu verlängern. Da ich es einfach nicht schaffe eins von beidem zu tun fallen ständig Gebühren an.

Der bibli-o-mat löst dieses Problem.

## Wie denn?

Drei Tage vor dem Fälligkeitsdatum (das ist ein Tag bevor die Bücherei sich meldet) werden alle fälligen Medien verlängert. Im Anschluss wird eine Auflistung der verlängerten Medien sowie einigen weiteren Infos an die hinterlegte Email Adresse geschickt.

Da nicht jeder mit diesem Problem auch die Möglichkeit hat einen Rechner zu betreiben auf dem bibli-o-mat regelmäßig läuft, kann der bibli-o-mat mehrere Accounts gleichzeitig verwalten. So sind Freunde und Bekannte auch gleich mit dabei.

## Was brauche ich dafür?
* Einen Bibliotheksausweis bei einer der folgenden Büchereien:  
  https://metropol-mediensuche.de/libraries
* Einen Mailtrap Account mit eigener Domain und bestandenem DKIM Check

## Install

### Clone source
* git clone && cd bibli-o-mat
* Setup dependencies: `poetry shell && poetry install`
* Test: `bibli-o-mat --help`


### Docker 
* Pull latest image: `docker pull ghcr.io/derhuerst/bibli-o-mat:main`
* `docker run -it --rm -v $PWD:/usr/app/data" ghcr.io/derhuerst/bibli-o-mat:main --help`

### Docker Compose
* Start Ofelia scheduler with `docker-compose -f docker_compose.yaml up -d`

## Configuration

First aus `add-user` to add a user to the bibli-o-mat. See the documentation below to get more information about the parameters. Each user is stored in a local database in the `data` folder. The database is created automatically. You can also add more users later.

Use the `renew` command to renew all due (3 days before deadline) media. the command takes a list of user names as parameter.

# CLI

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add-user`: Add a new user to bibli-o-mat.
* `list-due`: List due media of a user.
* `list-lent`: List all lent media of a user.
* `list-renewable`: List renewable media of a user.
* `list-users`: list all bibli-o-mat users.
* `renew`: Auto renew all due renewable media of all...

## `add-user`

Add a new user to bibli-o-mat.

Args:
    name (str): Name of the user use unique names.
    mail (str): email address of the user.
    id (str): Library card number.
    password (str): passwort of the user. Defaults to the card owners birthdate.

**Usage**:

```console
$ add-user [OPTIONS] NAME MAIL ID PASSWORD
```

**Arguments**:

* `NAME`: [required]
* `MAIL`: [required]
* `ID`: [required]
* `PASSWORD`: [required]

**Options**:

* `--help`: Show this message and exit.

## `list-due`

List due media of a user. A medium is due if it is three days before
the deadline.

Args:
    user_name (str): Name of the user (the first parameter of add-user)

**Usage**:

```console
$ list-due [OPTIONS] USER_NAME
```

**Arguments**:

* `USER_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `list-lent`

List all lent media of a user. There is also an indicator if the medium
is renewable.

   Args:
        user_name (str): Name of the user (the first parameter of add-user)

**Usage**:

```console
$ list-lent [OPTIONS] USER_NAMES...
```

**Arguments**:

* `USER_NAMES...`: [required]

**Options**:

* `--help`: Show this message and exit.

## `list-renewable`

List renewable media of a user. A medium is for example not renewable
if it is already renewed 3 times.

Args:
    user_name (str): Name of the user (the first parameter of add-user)

**Usage**:

```console
$ list-renewable [OPTIONS] USER_NAME
```

**Arguments**:

* `USER_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `list-users`

list all bibli-o-mat users.
    

**Usage**:

```console
$ list-users [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `renew`

Auto renew all due renewable media of all and send a info mail.

Args:
    user_name (str): Name of the user (the first parameter of add-user)

**Usage**:

```console
$ renew [OPTIONS] USER_NAMES...
```

**Arguments**:

* `USER_NAMES...`: [required]

**Options**:

* `--help`: Show this message and exit.

