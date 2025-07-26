"""
Script para consultar todos los assets, obtener sus dispositivos y la telemetría de los que empiezan con 'EM'.
Guarda los resultados en un archivo CSV.
"""
from lumenonpremise.auth import AuthClient
from lumenonpremise.assets import AssetClient
from lumenonpremise.relations import RelationClient
from lumenonpremise.telemetry import TelemetryClient
import csv
from datetime import datetime, timezone, timedelta

# Define la zona horaria UTC-6
TIMEZONE = timezone(timedelta(hours=-6))

def convert_utc_ms_to_local_str(utc_ms):
    if not utc_ms or not str(utc_ms).isdigit():
        return ""
    dt_utc = datetime.fromtimestamp(int(utc_ms) / 1000, tz=timezone.utc)
    dt_local = dt_utc.astimezone(TIMEZONE)
    return dt_local.strftime("%Y-%m-%d %H:%M:%S")

def main():
    auth = AuthClient()
    auth.login()
    asset_client = AssetClient(auth)
    relation_client = RelationClient(auth)
    telemetry_client = TelemetryClient(auth)

    assets = asset_client.get_all_assets()
    asset_list = assets.get('data', [])

    if not asset_list:
        print("No se encontraron assets.")
        auth.logout()
        return

    csv_filename = "em_telemetry.csv"
    with open(csv_filename, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "comercio_id", "comercio_nombre",
            "dispositivo_id", "dispositivo_nombre",
            "energyCount_ts", "energyCount_value",
            "deltaEnergyCount_ts", "deltaEnergyCount_value"
        ])

        for asset in asset_list:
            asset_id = asset['id']['id']
            asset_name = asset['name']
            asset_type = asset['id']['entityType']

            parameters = {
                "rootId": asset_id,
                "rootType": asset_type,
                "direction": "FROM",
                "relationTypeGroup": "COMMON",
                "maxLevel": 1,
                "fetchLastLevelOnly": False
            }
            filters = [
                {"relationType": "Contains", "entityTypes": ["DEVICE"]}
            ]

            try:
                relations_info = relation_client.get_relations_info(parameters, filters)
                for relation in relations_info:
                    to_entity = relation.get('to', {})
                    device_id = to_entity.get('id')
                    device_name = relation.get('toName', '')
                    if device_name.startswith("EM"):
                        keys = ['energyCount', 'deltaEnergyCount']
                        telemetry = telemetry_client.get_keys_values(device_id, keys)
                        # Extraer los datos para cada key
                        energyCount_ts = ""
                        energyCount_value = ""
                        deltaEnergyCount_ts = ""
                        deltaEnergyCount_value = ""

                        if 'energyCount' in telemetry and telemetry['energyCount']:
                            ec = telemetry['energyCount'][0]
                            energyCount_ts = convert_utc_ms_to_local_str(ec.get('ts', ''))
                            energyCount_value = ec.get('value', '')
                        if 'deltaEnergyCount' in telemetry and telemetry['deltaEnergyCount']:
                            dec = telemetry['deltaEnergyCount'][0]
                            deltaEnergyCount_ts = convert_utc_ms_to_local_str(dec.get('ts', ''))
                            deltaEnergyCount_value = dec.get('value', '')

                        writer.writerow([
                            asset_id, asset_name,
                            device_id, device_name,
                            energyCount_ts, energyCount_value,
                            deltaEnergyCount_ts, deltaEnergyCount_value
                        ])
            except Exception as e:
                print(f"Error al obtener info de relaciones o telemetría: {e}")

    print(f"Datos guardados en {csv_filename}")
    auth.logout()

if __name__ == "__main__":
    main()