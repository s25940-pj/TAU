import unittest
from flask import json
from app import app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreater(len(response.json), 0)

    def test_post_new_user(self):
        new_user = {
            "id": 3,
            "name": "Adam Smith",
            "email": "adam@smith.com"
        }
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        
    def test_post_new_user_with_invalid_data(self):
        new_user = {
            "id": 4
        }
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 500)

    def test_get_user_by_id(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"})
        
    def test_get_user_by_non_existing_id(self):
        response = self.app.get('/users/100')
        self.assertEqual(response.status_code, 500)

    def test_put_user(self):
        updated_user = {
            "id": 1,
            "name": "Jan Kowalski Updated",
            "email": "jan@kowalski_updated.pl"
        }
        response = self.app.put('/users/1', json=updated_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], updated_user["name"])
        self.assertEqual(response.json["email"], updated_user["email"])
    
    def test_put_non_existing_user(self):
        updated_user = {
            "id": 10,
            "name": "Alfred Bobinsky",
            "email": "alfred@bobinsky.com"
        }
        response = self.app.put('/users/100', json=updated_user)
        self.assertEqual(response.status_code, 500)

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
