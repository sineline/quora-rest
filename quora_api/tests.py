from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
#from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
import requests 
from rest_framework import status


class UserCreateTests(APITestCase):
    #factory = APIRequestFactory()
    api_auth = "/api/token-auth/"
    base_url = "http://localhost:8000"
    url_auth = base_url + api_auth

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.token = Token.objects.create(user=self.user)

        #print("Token:"+str(self.token))

    def testAuthFailed(self):
        username = "test"
        password = "12345678"
        param = {
            'username':username,
            'password':password,
        }

        # True API
        result = requests.post(url=self.url_auth, data=param)
        self.assertTrue(status.is_client_error(result.status_code))
        
        # Test API
        self.assertFalse(self.client.login(username=username, password=param.get(password)))
        
    def testAuthSuccess(self):
        param = {
            'username':"root",
            'password':"root",
        }

        # True API
        result = requests.post(url=self.url_auth, data=param)
        #self.true_token = result.json()['token']
        self.assertTrue(status.is_success(result.status_code))
        
        # Test API
        self.assertTrue(self.client.login(username='admin', password='admin123456'))

    def testCallUserAPI(self):
        url_api_user = self.base_url + "/api/users/"

        param = {
            'username':"root",
            'password':"root",
        }

        # True API
        result = requests.post(url=self.url_auth, data=param)
        true_token = result.json()['token']

        # True API
        result = requests.get(url_api_user, headers={'Authorization': 'Token '+true_token})
        self.assertTrue(status.is_success(result.status_code))
        
        # Test API
        #self.assertTrue(self.client.login(username='admin', password='admin123456'))
        
