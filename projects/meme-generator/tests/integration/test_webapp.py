import os
import tempfile
from flask import Flask
import pytest
import random
from flask.testing import FlaskClient
from app import app as flask_app
import re
from os import PathLike
import requests_mock
import filecmp
import operator
from PIL import Image, ImageChops


@pytest.fixture
def client() -> FlaskClient:
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def get_html(response):
    """Extract the html from a flask response, as a string."""
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    return response.data.decode("utf-8")


def check_meme_image(client: FlaskClient, html: str, expected_img_file: PathLike):
    """Check check a meme image within the meme page, against an expected local image file."""
    m = re.compile('<img src="static\\/(meme-[^\\.]+\\.jpg)" \\/>').search(html)
    assert m is not None
    img_name = m.group(1)
    img_response = client.get(f"static/{img_name}")
    assert img_response.status_code == 200
    assert img_response.content_type == "image/jpeg"
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tf:
        tf.write(img_response.data)
        with Image.open(tf.name) as actual_img, Image.open(
            f"./tests/_data/{expected_img_file}"
        ) as expected_img:
            img_diff = ImageChops.difference(actual_img, expected_img)
            assert img_diff.getbbox() is None


def test_homepage(client: FlaskClient, monkeypatch):
    """Test loading the home page.

    Compares the returned image with the expected one based on a
    fixed random seed.
    """
    random.seed(42)
    monkeypatch.setattr(random, "choice", operator.itemgetter(0))
    response = client.get("/")
    html = get_html(response)
    assert "<title>Meme Generator</title>" in html
    check_meme_image(client, html, "expected_homepage_meme.jpg")


def test_create(client: FlaskClient):
    """Test creating a user defined meme."""
    random.seed(42)
    external_img_url = "http://localhost/images/black.bmp"
    with requests_mock.Mocker() as m, open("./tests/_data/black.bmp", "rb") as f:
        m.get(external_img_url, headers={"content-type": "image/x-ms-bmp"}, body=f)
        response = client.post(
            "/create",
            data={
                "image_url": external_img_url,
                "body": "Veni, vidi, vici.",
                "author": "Julius Caesar",
            },
        )
    html = get_html(response)
    check_meme_image(client, html, "expected_user_meme.jpg")
