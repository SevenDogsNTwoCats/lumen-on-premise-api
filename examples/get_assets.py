
"""
Example script to authenticate and retrieve asset information from the API.
Shows how to list all assets and get details for the first asset found.
"""
from lumenonpremise.auth import AuthClient
from lumenonpremise.assets import AssetClient

def main():
    """
    Authenticate, retrieve all assets, print their summary, and show details for the first asset found.
    """
    auth = AuthClient()
    auth.login()
    asset_client = AssetClient(auth)

    assets = asset_client.get_all_assets()
    print("\n--- Assets Obtenidos ---")
    print("Tipo  | ID                                   | Nombre")
    for asset in assets.get("data", []):
        print(f"{asset['id']['entityType']} | {asset['id']['id']} | {asset['name']}")


    asset_name = assets['data'][0]['name'] if assets['data'] else None
    if asset_name:
        asset = asset_client.get_asset_by_name(asset_name)
        print(f"\n--- Detalles del Activo '{asset_name}' ---")
        print(asset)
    else:
        print("No se encontraron activos para mostrar detalles.")

    auth.logout()

if __name__ == "__main__":
    main()