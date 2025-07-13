import requests
from lumenonpremise.auth import AuthClient
from lumenonpremise.config import BASE_URL

class TelemetryClient:
    """
    Client for telemetry data API operations.
    """
    def __init__(self, auth_client: AuthClient):
        """
        Initialize TelemetryClient with an AuthClient instance.
        Args:
            auth_client (AuthClient): The authentication client.
        """
        self.auth_client = auth_client

    def get_keys_values(self, device_id: str, keys: list):
        """
        Get timeseries values for specified keys of a device.
        Args:
            device_id (str): ID of the device.
            keys (list): List of keys to retrieve.
        Returns:
            dict: JSON response containing key values.
        Raises:
            Exception: If the request fails.
        """
        keys_param = ",".join(keys)
        url = f"{BASE_URL}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries?keys={keys_param}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener valores instantáneos: {response.status_code} - {response.text}")

    def get_consumption_delta(self, device_id: str, key: str, start_ts: int, end_ts: int, interval: int):
        """
        Get consumption delta for a key over a time interval.
        Args:
            device_id (str): ID of the device.
            key (str): Key to retrieve.
            start_ts (int): Start timestamp.
            end_ts (int): End timestamp.
            interval (int): Aggregation interval.
        Returns:
            dict: JSON response containing delta values.
        Raises:
            Exception: If the request fails.
        """
        url = (
            f"{BASE_URL}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries"
            f"?keys={key}&startTs={start_ts}&endTs={end_ts}&interval={interval}&agg=DELTA"
        )
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener consumo acumulado (DELTA): {response.status_code} - {response.text}")

    def get_consumption_sum(self, device_id: str, key: str, start_ts: int, end_ts: int, interval: int):
        """
        Get consumption sum for a key over a time interval.
        Args:
            device_id (str): ID of the device.
            key (str): Key to retrieve.
            start_ts (int): Start timestamp.
            end_ts (int): End timestamp.
            interval (int): Aggregation interval.
        Returns:
            dict: JSON response containing sum values.
        Raises:
            Exception: If the request fails.
        """
        url = (
            f"{BASE_URL}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries"
            f"?keys={key}&startTs={start_ts}&endTs={end_ts}&interval={interval}&agg=SUM"
        )
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener consumo por suma (SUM): {response.status_code} - {response.text}")

    def get_available_keys(self, device_id: str):
        """
        Get available telemetry keys for a device.
        Args:
            device_id (str): ID of the device.
        Returns:
            dict: JSON response containing available keys.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/plugins/telemetry/DEVICE/{device_id}/keys/timeseries"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener claves disponibles: {response.status_code} - {response.text}")
