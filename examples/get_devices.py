
"""
Example script to authenticate and retrieve device information from the API.
Shows how to list all devices, get details and credentials for the first device found.
"""
from lumenonpremise.auth import AuthClient
from lumenonpremise.devices import DeviceClient

def main():
    """
    Authenticate, retrieve all devices, print their summary, and show details and credentials for the first device found.
    """
    auth = AuthClient()
    auth.login()
    device_client = DeviceClient(auth)

    devices = device_client.get_all_devices()
    print("\n--- Dispositivos Obtenidos ---")
    print("Tipo   | ID                                   | Nombre")
    for device in devices.get("data", []):
        print(f"{device['id']['entityType']} | {device['id']['id']} | {device['name']}")

    device_name = devices['data'][0]['name'] if devices['data'] else None
    if device_name:
        device = device_client.get_device_by_name(device_name)
        print(f"\n--- Detalles del Dispositivo '{device_name}' ---")
        print(device)
    else:
        print("No se encontraron dispositivos para mostrar detalles.")

    device_id = devices['data'][0]['id']['id'] if devices['data'] else None
    if device_id:

        device_details = device_client.get_device_by_id(device_id)
        print(f"\n--- Dettalles del Dispositivo con ID '{device_id}' ---")
        print(device_details)

        device_credentials = device_client.get_device_credentials(device_id)
        print(f"\n--- Credenciales del Dispositivo con ID '{device_id}' ---")
        print(device_credentials)
    else:
        print("No se encontraron dispositivos para mostrar credenciales.")

    auth.logout()

if __name__ == "__main__":
    main()