import requests
from lumenonpremise.config import BASE_URL, USERNAME, PASSWORD

class AuthClient:
    """
    Handles authentication and token management for API requests.
    """
    def __init__(self):
        """
        Initialize AuthClient with token attributes.
        """
        self.token = None
        self.refresh_token = None

    def login(self):
        """
        Authenticate with the API and retrieve access and refresh tokens.
        Raises:
            Exception: If authentication fails.
        """
        url = f"{BASE_URL}/api/auth/login"
        payload = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data["token"]
            self.refresh_token = data["refreshToken"]
            print("✅ Login exitoso")
        else:
            raise Exception(f"Error de login: {response.status_code} - {response.text}")

    def get_headers(self):
        """
        Get authorization headers for authenticated requests.
        Returns:
            dict: Headers with Bearer token.
        Raises:
            Exception: If token is not available.
        """
        if not self.token:
            raise Exception("Token no disponible. ¿Olvidaste llamar a login()?")
        return {
            "X-Authorization": f"Bearer {self.token}"
        }

    def refresh(self):
        """
        Refresh the authentication token using the refresh token.
        Raises:
            Exception: If token refresh fails.
        """
        url = f"{BASE_URL}/api/auth/token"
        payload = {
            "refreshToken": self.refresh_token
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            self.token = data["token"]
            self.refresh_token = data["refreshToken"]
            print("🔄 Token renovado")
        else:
            raise Exception(f"Error al renovar token: {response.status_code} - {response.text}")

    def logout(self):
        """
        Log out and invalidate the current session.
        Raises:
            Exception: If logout fails.
        """
        url = f"{BASE_URL}/api/auth/logout"
        headers = self.get_headers()
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print("👋 Sesión cerrada correctamente")
        else:
            raise Exception(f"Error al cerrar sesión: {response.status_code} - {response.text}")
