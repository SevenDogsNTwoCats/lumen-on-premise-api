import requests
from lumenonpremise.auth import AuthClient
from lumenonpremise.config import BASE_URL

class DeviceClient:
    """
    Client for device-related API operations.
    """
    def __init__(self, auth_client: AuthClient):
        """
        Initialize DeviceClient with an AuthClient instance.
        Args:
            auth_client (AuthClient): The authentication client.
        """
        self.auth_client = auth_client

    def get_all_devices(self, pageSize=100, page=0):
        """
        Retrieve all devices with pagination.
        Args:
            pageSize (int): Number of devices per page.
            page (int): Page number.
        Returns:
            dict: JSON response containing device data.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/tenant/devices?pageSize={pageSize}&page={page}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener dispositivos: {response.status_code} - {response.text}")

    def get_device_by_name(self, name):
        """
        Retrieve device details by name.
        Args:
            name (str): Name of the device.
        Returns:
            dict: JSON response containing device details.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/tenant/devices?deviceName={name}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener dispositivo por nombre: {response.status_code} - {response.text}")

    def get_device_by_id(self, device_id):
        """
        Retrieve device details by ID.
        Args:
            device_id (str): ID of the device.
        Returns:
            dict: JSON response containing device details.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/device/{device_id}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener dispositivo por ID: {response.status_code} - {response.text}")

    def get_device_credentials(self, device_id):
        """
        Retrieve credentials for a device by ID.
        Args:
            device_id (str): ID of the device.
        Returns:
            dict: JSON response containing device credentials.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/device/{device_id}/credentials"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener credenciales del dispositivo: {response.status_code} - {response.text}")
