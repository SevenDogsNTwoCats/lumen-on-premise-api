import requests
from lumenonpremise.auth import AuthClient
from lumenonpremise.config import BASE_URL

class RelationClient:
    """
    Client for entity relation API operations.
    """
    def __init__(self, auth_client: AuthClient):
        """
        Initialize RelationClient with an AuthClient instance.
        Args:
            auth_client (AuthClient): The authentication client.
        """
        self.auth_client = auth_client

    def get_relations_from(self, entity_id: str, entity_type: str):
        """
        Get relations from a given entity.
        Args:
            entity_id (str): ID of the source entity.
            entity_type (str): Type of the source entity.
        Returns:
            dict: JSON response containing relations.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/relation/query?fromId={entity_id}&fromType={entity_type}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener relaciones desde entidad: {response.status_code} - {response.text}")

    def get_relations_to(self, entity_id: str, entity_type: str):
        """
        Get relations to a given entity.
        Args:
            entity_id (str): ID of the target entity.
            entity_type (str): Type of the target entity.
        Returns:
            dict: JSON response containing relations.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/relation/query?toId={entity_id}&toType={entity_type}"
        headers = self.auth_client.get_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener relaciones hacia entidad: {response.status_code} - {response.text}")

    def get_relations_info(self, parameters: dict, filters: list = None):
        """
        Get detailed relations info using a POST body.
        Args:
            parameters (dict): Parameters for the query (rootId, rootType, direction, etc).
            filters (list, optional): List of filter dicts.
        Returns:
            dict: JSON response containing relations info.
        Raises:
            Exception: If the request fails.
        """
        url = f"{BASE_URL}/api/relations/info"
        headers = self.auth_client.get_headers()
        headers["Content-Type"] = "application/json"
        body = {
            "parameters": parameters,
            "filters": filters if filters is not None else []
        }
        response = requests.post(url, json=body, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener info de relaciones: {response.status_code} - {response.text}")
