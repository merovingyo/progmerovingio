import sqlite3

import pytest

@pytest.fixture(scope='function')
def db():
    
    conn = sqlite3.connect(':memory:')
    
    cursor = conn.cursor()
    
    cursor.execute('''
	    CREATE TABLE coinchain
        (account text, moeda real, date text)''')
    
    sample_data = [
        ('152152', 45.0, '2025-05-03'),
        ('452885', 150.0, '2025-05-10'),
    ]
    
    cursor.executemany('INSERT INTO coinchain VALUES(?, ?, ?)', sample_data)
    
    yield conn
    

def test_connection(db):

    cursor = db
    assert len(list(cursor.execute('SELECT * FROM coinchain'))) == 2


def tearDown():
    pass

def test_sum_values(setUp):
    
    query = "INSERT INTO coinchain (id, title, text) VALUES (?, ?, ?)"
    
    values = (1, "365251", "2512.5")
    
    db.execute(query, values)
    
    assert 1 + 1  == 2

@pytest.mark.skip(reason="Not implemented yet")
def test_test():
    print("teste >>>>>>>>>>")
    pass