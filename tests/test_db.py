from flaskr.db import get_db
import sqlite3
import pytest

def test_get_close_db(app):
	with app.app_context():
		db = get_db()
		assert db is get_db()

	with pytest.raises(sqlite3.ProgrammingError) as e:
		db.execute('select 1')

	assert 'closed' in str(e.value)
