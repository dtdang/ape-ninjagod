import click
from ape.cli import existing_alias_argument

import typer

# @click.group
# def cli():
#     """Hello ape-ninjagod"""

cli = typer.Typer()

@cli.command()
def top():
   """
   typer top level
   """

@cli.callback()
def callback():
   """
   typer with click
   """

@click.command()
def my_sub_cmd():
    print("hello sub cmd")

@click.command()
@existing_alias_argument()
def get_existing(alias):
  click.echo(f"{alias} is an existing account!")

typer_click = typer.main.get_command(cli)
typer_click.add_command(get_existing)
typer_click.add_command(my_sub_cmd)

if __name__ == "__main__":
   typer_click()