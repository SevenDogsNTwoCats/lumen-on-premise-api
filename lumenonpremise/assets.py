import requests
from lumenonpremise.auth import AuthClient
from lumenonpremise.config import BASE_URL

class AssetClient:
    """
    Client for asset-related API operations.
    """
    def __init__(self, auth_client: AuthClient):
        """
        Initialize AssetClient with an AuthClient instance.
        Args:
            auth_client (AuthClient): The authentication client.
        """
        self.auth_client = auth_client

    def get_all_assets(self, pageSize=100, page=0):
        """
        Retrieve all assets with pagination.
        Args:
            pageSize (int): Number of assets per page.
            page (int): Page number.
        Returns:
            dict: JSON response containing asset data.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/tenant/assets?pageSize={pageSize}&page={page}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener activos: {response.status_code} - {response.text}")

    def get_asset_by_name(self, name):
        """
        Retrieve asset details by name.
        Args:
            name (str): Name of the asset.
        Returns:
            dict: JSON response containing asset details.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/tenant/assets?assetName={name}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener activo por nombre: {response.status_code} - {response.text}")
