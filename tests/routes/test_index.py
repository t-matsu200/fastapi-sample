# -*- coding: utf-8 -*-


def test_index(fixture_app_test):
    """インデックスルート"""
    client = fixture_app_test
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'state': {
            'client': {'user': {'name': None}},
            'server': {'host': 'testserver', 'port': None}
        }
    }


def test_404_error(fixture_app_test):
    """Not Found"""
    client = fixture_app_test
    response = client.get('/not-found')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
