import click

from secrets import choice
from string import ascii_letters, digits


TOKEN_CHARSET = ascii_letters + digits
TOKEN_LENGTH = 99
TOKEN_COUNT = 10
PREFIXES = ['dev_', 'test_', 'prod_']


@click.command()
@click.option('--length', default=TOKEN_LENGTH, show_default=True,
              help='Character length.')
@click.option('--count', default=TOKEN_COUNT, show_default=True,
              help='Generate N secrets.')
@click.option('--prefix', default=PREFIXES, show_default=True, multiple=True,
              help='1 or more key prefixes.')
def secrets(length, count, prefix):
    """
    Generate a set of random secret tokens.

    They are suitable for your SECRET_KEY, passwords, API keys and more.
    """
    for p in prefix:
        for i in range(count):
            click.echo(random_token(p, length))

    return None


def random_token(prefix, length=TOKEN_LENGTH):
    token = ''.join(choice(TOKEN_CHARSET) for i in range(length))
    return f"{prefix}{token}"
