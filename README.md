# bibli-o-mat 🤖

Mit den Kindern sind wir ständig in der Bücherei. Wenn die ausgeliehenen Medien fällig werden, bekommt man eine Mail und hat dann 2 Tage Zeit die Medien zurückzugeben oder zu verlängern. Da ich es einfach nicht schaffe eins von beidem zu tun fallen ständig Gebühren an.

Der bibli-o-mat löst dieses Problem.

## Wie denn?

Drei Tage vor dem Fälligkeitsdatum (das ist ein Tag bevor die Bücherei sich meldet) werden alle fälligen Medien verlängert. Im anschluss wird eine Mail mit einer Auflistung der verlängerten Medien sowie einigen weiteren Infos an die hinterlegte email Adresse geschickt. 

Da nicht jeder mit diesem Problem auch die Möglichkeit hat einen Server zu betreiben, kann der bibli-o-mat auch mit mehreren Accounts umgehen. Dann sind freunde und bekannte auch gleich mit abgedeckt.

## Was brauche ich dafür?
* Einen Bibliotheksausweis bei einer der folgenden Büchereien:  
  https://metropol-mediensuche.de/libraries
* Einen Mailtrap account mit eigener Domain und bestandenem DKIM check

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
* `renew`: Auto renew all due renewable media of a...

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
$ list-lent [OPTIONS] USER_NAME
```

**Arguments**:

* `USER_NAME`: [required]

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

Auto renew all due renewable media of a user and send a info mail.

Args:
    user_name (str): Name of the user (the first parameter of add-user)

**Usage**:

```console
$ renew [OPTIONS] USER_NAME
```

**Arguments**:

* `USER_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

