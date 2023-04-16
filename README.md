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

* `account-info`
* `add-user`
* `list-due`
* `list-lent`
* `list-renewable`
* `list-users`
* `renew`
* `user-token-refresh`

## `account-info`

**Usage**:

```console
$ account-info [OPTIONS]
```

**Options**:

* `--user-name TEXT`: [required]
* `--help`: Show this message and exit.

## `add-user`

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

**Usage**:

```console
$ list-due [OPTIONS]
```

**Options**:

* `--user-name TEXT`: [required]
* `--help`: Show this message and exit.

## `list-lent`

**Usage**:

```console
$ list-lent [OPTIONS]
```

**Options**:

* `--user-name TEXT`: [required]
* `--help`: Show this message and exit.

## `list-renewable`

**Usage**:

```console
$ list-renewable [OPTIONS]
```

**Options**:

* `--user-name TEXT`: [required]
* `--help`: Show this message and exit.

## `list-users`

**Usage**:

```console
$ list-users [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `renew`

**Usage**:

```console
$ renew [OPTIONS]
```

**Options**:

* `--user-name TEXT`: [required]
* `--help`: Show this message and exit.

## `user-token-refresh`

**Usage**:

```console
$ user-token-refresh [OPTIONS] CARD_NUMBER
```

**Arguments**:

* `CARD_NUMBER`: [required]

**Options**:

* `--help`: Show this message and exit.

