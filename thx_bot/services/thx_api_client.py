from base64 import b64encode

import requests

from thx_bot.models.channels import Channel
from thx_bot.models.users import User

URL_GET_TOKEN = "https://api.thx.network/token"
URL_ASSET_POOL_INFO = "https://api.thx.network/v1/asset_pools/"
URL_SIGNUP = "https://api.thx.network/v1/signup"


def get_token_auth_headers(client_id: str, client_secret: str) -> dict:
    auth_header_encoded = b64encode(f"{client_id}:{client_secret}".encode()).decode('utf-8')
    return {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f"Basic {auth_header_encoded}"
    }


def get_api_token(channel: Channel) -> str:
    response = requests.post(
        URL_GET_TOKEN,
        data={
            'grant_type': "client_credentials",
            'scope': "openid admin",
        },
        headers=get_token_auth_headers(channel.client_id, channel.client_secret)
    )
    return response.json()['access_token']


def get_asset_pool_info(channel: Channel) -> dict:
    response = requests.get(
        f"{URL_ASSET_POOL_INFO}{channel.pool_address}",
        headers={
            'Content-Type': "application/json",
            'Authorization': f"Bearer {get_api_token(channel)}",
        }
    )
    return response.json()


def signup_user(user: User, channel: Channel) -> dict:
    response = requests.post(
        URL_SIGNUP,
        data={
            'email': user.email,
            'password': user.password,
            'confirmPassword': user.password,
        },
        headers={
            'AssetPool': channel.pool_address,
            'Authorization': f"Bearer {get_api_token(channel)}",
        },
    )
    return response.json()
