import pytest
import requests


post_data = {'sendere_mail': 'sender@postdummy.com',
             'receiver_mail': 'receiver@postdummy.com',
             'weight': '18 kg',
             'traking_id': '123456',
             }


def get_post_data():
    # Making a POST request
    r = requests.post('https://httpbin.org/post', data=post_data)
    return r.json()['form']


def test_post_data():
    data = get_post_data()
    # print(data)
    assert data == post_data


if __name__ == '__main__':
    pytest.main([__file__])
