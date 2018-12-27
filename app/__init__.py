import click
import requests
from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='cyan')


@click.command()
@click.option('--category', '-c', type=click.Choice(
    ["dev", "movie", "food", "celebrity", "science", "sport", "political",
     "religion", "animal", "history", "music", "travel", "career", "money", "fashion"]))
def main(category):
    """
    If I had a nickel for every Chuck Norris joke out there...
    """

    if category:
        url = 'https://api.chucknorris.io/jokes/random?category={}'
    else:
        url = 'https://api.chucknorris.io/jokes/random'

    try:
        spinner.start()
        response = requests.get(url.format(category))
        spinner.stop()
        spinner.clear()
        click.echo(response.json()['value'])
    except requests.exceptions.ConnectionError:
        spinner.warn("You don't find Chuck Norris, Chuck Norris finds you!")
        click.echo("Looks like you're not connected to the internet 🤭")
    except requests.exceptions.Timeout:
        spinner.warn("You don't find Chuck Norris, Chuck Norris finds you!")
        click.echo("Your connection timed out!")
    except requests.exceptions.RequestException as e:
        spinner.fail()
        click.echo(e)
