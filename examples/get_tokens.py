
"""
Example script to authenticate and print access and refresh tokens from the API.
"""
from lumenonpremise.auth import AuthClient

def main():
    """
    Authenticate and print the access and refresh tokens.
    """
    auth = AuthClient()
    auth.login()

    print("\n--- Tokens Obtenidos ---")
    print("Access Token:", auth.token)
    print("Refresh Token:", auth.refresh_token)

    auth.logout()

if __name__ == "__main__":
    main()
