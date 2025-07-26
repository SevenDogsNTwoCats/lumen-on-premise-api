"""
Ejemplo para obtener las relaciones de un asset usando /api/relations/info.
"""
from lumenonpremise.auth import AuthClient
from lumenonpremise.assets import AssetClient
from lumenonpremise.relations import RelationClient

def main():
    auth = AuthClient()
    auth.login()
    asset_client = AssetClient(auth)
    relation_client = RelationClient(auth)

    assets = asset_client.get_all_assets()
    asset_list = assets.get('data', [])

    if not asset_list:
        print("No se encontraron assets.")
        auth.logout()
        return

    asset = asset_list[0]
    asset_id = asset['id']['id']
    asset_type = asset['id']['entityType']
    asset_name = asset['name']

    print(f"\n--- Devices de: {asset_name} (ID: {asset_id}) ---")

    parameters = {
        "rootId": asset_id, # ID del asset o entidad como un device
        "rootType": asset_type,  # "ASSET" o el tipo correspondiente como "DEVICE"
        "direction": "FROM",  # o TO
        "relationTypeGroup": "COMMON",
        "maxLevel": 1, # Nivel máximo de relaciones a obtener, 1 es el nivel directo
        "fetchLastLevelOnly": False # Si es True, solo devuelve las relaciones del último nivel
    }
    filters = [
        # Puedes agregar filtros si lo necesitas, por ejemplo:
        {"relationType": "Contains", "entityTypes": ["DEVICE"]}
    ]

    try:
        relations_info = relation_client.get_relations_info(parameters, filters)
        print("Type   | id")
        print("-------------------------------")
        for relation in relations_info:
            to_entity = relation.get('to', {})
            print(f"{to_entity.get('entityType', 'Desconocida')} | {to_entity.get('id', 'Desconocida')}")
    except Exception as e:
        print(f"Error al obtener info de relaciones: {e}")

    auth.logout()

if __name__ == "__main__":
    main()