import click
from ape.cli import existing_alias_argument


@click.group
def cli():
    """Hello ape-ninjagod"""


@cli.command()
def my_sub_cmd():
    print("hello sub cmd")

@click.command()
@existing_alias_argument()
def my_cmd(alias):
  click.echo(f"{alias} is an existing account!")