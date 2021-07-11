import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1, database_url=os.getenv("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up section
    application = create_application()
    application.dependency_overrides[get_settings] = get_settings_override
    with TestClient(application) as test_client:
        # testing section
        yield test_client
    # teardown section


@pytest.fixture(scope="module")
def test_app_with_db():
    # set up section
    application = create_application()
    application.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(application) as test_client:
        # testing section
        yield test_client

    # teardown section
