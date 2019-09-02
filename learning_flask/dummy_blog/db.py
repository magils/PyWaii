import sqlite3
from flask import current_app,g
import click
from flask.cli import with_appcontext


def init_app(app):

     #This function is going to be call when cleaning up after returning a response
     app.teardown_appcontext(close_db)

     # This is going to execute this function everytime a terminal `flask` command is executed
     app.cli.add_command(init_db_command)


def get_db():

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as schema_file:
        db.executescript(schema_file.read().decode("utf-8"))

#This method would can be called from the terminal
@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database")
