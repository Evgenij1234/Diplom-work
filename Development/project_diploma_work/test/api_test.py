import unittest
import requests

#Указать домен запуска машины на которой запущен докер
BASE_URL = 'http://192.168.0.104:5000'

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'password123'
        self.token = None

    def test_01_register(self):
        response = requests.post(f'{BASE_URL}/register', json={
            'username': self.username,
            'password': self.password
        })
        self.assertIn(response.status_code, [201, 409]) 
        if response.status_code == 201:
            self.assertIn('access_token', response.json())
            self.token = response.json()['access_token']

    def test_02_login(self):
        response = requests.post(f'{BASE_URL}/login', json={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json())
        self.token = response.json()['access_token']

    def test_03_protected_valid_token(self):
        self.test_02_login()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{BASE_URL}/protected', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_04_protected_no_token(self):
        response = requests.get(f'{BASE_URL}/protected')
        self.assertEqual(response.status_code, 401)

    def test_05_validate_token(self):
        self.test_02_login()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{BASE_URL}/validate-token', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get('valid'))

    def test_06_files_not_found(self):
        response = requests.get(f'{BASE_URL}/files/{self.username}')
        self.assertIn(response.status_code, [404, 200])

    def test_07_products_missing_param(self):
        response = requests.get(f'{BASE_URL}/products')
        self.assertEqual(response.status_code, 400)

    def test_08_products_with_param(self):
        self.test_02_login()
        params = {'user': self.username}
        response = requests.get(f'{BASE_URL}/products', params=params)
        self.assertIn(response.status_code, [200, 404])

    def test_09_scrape_endpoint(self):
        response = requests.post(f'{BASE_URL}/scrape/{self.username}')
        self.assertIn(response.status_code, [200, 400, 404, 500])

    def test_10_savedb_file_not_found(self):
        response = requests.post(f'{BASE_URL}/savedb/{self.username}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
