# LUMEN On-Premise API Client

This project provides a Python client implementation and usage examples for interacting with the LUMEN On-Premise API. It includes modules for authentication, asset management, device management, relations, and telemetry data retrieval.

## Features

- Authenticate and manage API tokens
- Retrieve and manage assets
- Retrieve and manage devices
- Query entity relations
- Fetch telemetry data

## Requirements

- Python 3.8+
- `requests` library
- `python-dotenv` for environment variable management

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/SevenDogsNTwoCats/lumen-on-premise-api
   cd lumen-on-premise-api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```env
   BASE_URL=https://your-lumen-api-url
   LUMEN_USERNAME=your-username
   PASSWORD=your-password
   ```

## Usage

Example scripts are provided in the `examples/` directory:

- `get_assets.py`: List all assets and show details for the first asset.
- `get_devices.py`: List all devices, show details and credentials for the first device.
- `get_telemetry.py`: Fetch available telemetry keys and instant values for the first device.
- `get_tokens.py`: Authenticate and print access/refresh tokens.

Run any example script:
```sh
python -m examples.get_assets
```

## Project Structure

```
lumenonpremise/
    auth.py           # Authentication and token management
    assets.py         # Asset management
    devices.py        # Device management
    relations.py      # Entity relations
    telemetry.py      # Telemetry data retrieval
    config.py         # Configuration loader
examples/
    get_assets.py     # Example: asset operations
    get_devices.py    # Example: device operations
    get_telemetry.py  # Example: telemetry operations
    get_tokens.py     # Example: token retrieval
```

## Documentation

All modules and functions are documented with English docstrings. See the source code for details on usage and parameters.

## License

MIT License
