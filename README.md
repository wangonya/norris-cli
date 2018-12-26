# norris-cli
A simple cli app that brightens up your day with Chuck Norris jokes from [chucknorris.io](https://api.chucknorris.io/).

## Installation
Install norris-cli from PyPi
```
pip install norris-cli
```

## How to use
```
$ norris-cli --help
Usage: norris-cli [OPTIONS]

  If I had a nickel for every Chuck Norris joke out there...

Options:
  -c, --category [dev|movie|food|celebrity|science|sport|political|religion|animal|history|music|travel|career|money|fashion]
  --help                          Show this message and exit.

```

### Get a random joke
```
$ norris-cli
Chuck Norris doesn't call the wrong number. You answer the wrong phone.
```

### Specify a category
_You can see all available categories by running `norris-cli --help`_
```
$ norris-cli -c dev
Chuck Norris can't test for equality because he has no equal.
```

```
$ norris-cli -c food
Chuck Norris' favorite cereal is Kellogg's Nails 'N' Gravel.
```

Enjoy!

![approval](https://media.giphy.com/media/3hvmlYNsOTFWE/giphy.gif)