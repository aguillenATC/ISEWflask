import pytest
from flask import g
from flask import session

from isew.db import get_db


def test_register(client, app):
    # comprobamos código de respuesta correcto para página de registro
    assert client.get("/auth/register").status_code == 200

    # test tras registro existoso volvemos a login
    response = client.post("/auth/register", data={"username": "a", "password": "a"})
    assert "http://localhost/auth/login" == response.headers["Location"]

    # test que el usuario está añadido a la BD
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM usuario WHERE nombre = 'a'").fetchone()
            is not None
        )
