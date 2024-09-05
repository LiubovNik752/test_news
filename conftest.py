import psycopg2
from allure import step
import pytest

from conf import host, db_user, db_password, db_database, port
from postgresql_connection import POSTGRESQL


@pytest.fixture(scope="class")
def db_connect():
    log_text = 'Create Postgres connection...'
    with step(log_text):
        test_db = POSTGRESQL(
            host=host,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database,
            port=port
        )
        # test_db.log.debug(log_text)
        yield test_db

    del test_db
