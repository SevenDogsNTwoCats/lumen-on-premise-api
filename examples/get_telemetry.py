
"""
Example script to authenticate and retrieve telemetry information for a device from the API.
Shows how to get available telemetry keys and fetch instant values for the first device found.
"""
from lumenonpremise.auth import AuthClient
from lumenonpremise.devices import DeviceClient
from lumenonpremise.telemetry import TelemetryClient

def main():
    """
    Authenticate, retrieve available telemetry keys for the first device, and print instant values for up to three keys.
    """
    auth = AuthClient()
    auth.login()
    device_client = DeviceClient(auth)
    telemetry_client = TelemetryClient(auth)

    devices = device_client.get_all_devices()
    device_id = devices['data'][0]['id']['id'] if devices['data'] else None

    if device_id:
        # Obtener las claves disponibles de telemetría
        keys = telemetry_client.get_available_keys(device_id)
        print("\n--- Claves de Telemetría Disponibles ---")
        print(keys)

        # Obtener los valores instantáneos de las primeras 3 claves
        keys_list = keys[:3] if isinstance(keys, list) else []
        if keys_list:
            telemetry = telemetry_client.get_keys_values(device_id, keys_list)
            print(f"\n--- Telemetría instantánea para {keys_list} ---")
            print(telemetry)
        else:
            print("No hay claves de telemetría disponibles para este dispositivo.")
    else:
        print("No se encontró ningún dispositivo.")

    auth.logout()

if __name__ == "__main__":
    main()