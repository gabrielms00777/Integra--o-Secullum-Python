import requests
import os
import json

TOKEN_FILE = 'token.json'

class APIConfig:
    def __init__(self, auth_url, api_url, username, password, client_id="3") -> None:
        self.auth_url = auth_url
        self.api_url = api_url
        self.username = username
        self.password = password
        self.client_id = client_id
        self.token = self.load_token()
        self.selected_bank_id = None

    def load_token(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'r') as file:
                data = json.load(file)
                token = data.get('access_token')
                if token and self.verify_token(token):
                    return token
                
        return self.authenticate()
    
    def verify_token(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        try:
            data = {
                "token": token
            }
            response = requests.post(f"{self.auth_url}/ReinvidicacoesToken",data=data, headers=headers)
            # print(response.json()) Depois salvar os dados do usuario no token
            return response.ok
        
        except requests.RequestException:
            return False

    def authenticate(self):
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(f"{self.auth_url}/Token", data=data, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        self.save_token(token_data)
        return token_data['access_token']

    def save_token(self, token_data):
        with open(TOKEN_FILE, "w") as file:
            json.dump(token_data, file)

    def set_bank_id(self, bank_id):
        self.selected_bank_id = bank_id

    def get_headers(self):
        headers = {"Authorization": f"Bearer {self.token}"}

        if self.selected_bank_id:
            headers['secullumidbancoselecionado'] = str(self.selected_bank_id)

        return headers
    
    def verify_file_exists(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"O arquivo {filename} não foi encontrado no diretório.")
    
    def get(self, endpoint, params = None):
        headers = self.get_headers()
        response = requests.get(f"{self.api_url}/{endpoint}",params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data):
        headers = self.get_headers()
        response = requests.post(f"{self.api_url}/{endpoint}",json=data, headers=headers)
        response.raise_for_status()
        return response.status_code
    
    def put(self, endpoint, data):
        headers = self.get_headers()
        response = requests.put(f"{self.api_url}/{endpoint}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        headers = self.get_headers()
        response = requests.delete(f"{self.api_url}/{endpoint}", headers=headers)
        response.raise_for_status()
        return response.status_code

