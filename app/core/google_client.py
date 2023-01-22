from pprint import pprint

from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds

from app.core.config import settings

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
# INFO = {
#     'type': settings.type,
#     'project_id': settings.project_id,
#     'private_key_id': settings.private_key_id,
#     'private_key': settings.private_key,
#     'client_email': settings.client_email,
#     'client_id': settings.client_id,
#     'auth_uri': settings.auth_uri,
#     'token_uri': settings.token_uri,
#     'auth_provider_x509_cert_url': settings.auth_provider_x509_cert_url,
#     'client_x509_cert_url': settings.client_x509_cert_url
# }
INFO = {
    "type": "service_account",
    "project_id": "alert-synapse-375418",
    "private_key_id": "1ee696e58dc8a62b205b4253081494eebcfeb0ed",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBvl1Vuo8HgK0T\np5hJU/0bxNBVH1wdPXzdzJhfmQ7aLHCmSEqn2kr+Ug0bqC9To53d7/NimB7llXT9\nTVk0cGG9iS+qspcfhIoP92x9JS2FzTp0Z0u+vrHqSBgL/Xb5d+oxtC6iKYylvI9a\nONYz9YGH1RBDRvG4wVeDGMxkC+Rf72u1ST/Hm8WMDLeGjA6gtFXYkkQI8Fws4Y+3\nXfy1sjpxQTSX2isI0zcf4X6MXc7uDh0130vWbnCWAUbp/FNoWDW5+2x6WXniy4Ic\njD0bsB7WMz6yb7M/HZJ0pBFCkaoklqWpjA6IyuZ3Vrg5ITUippdokhWVFAormiYz\nObuo2gsfAgMBAAECggEALXr7HQtQ1SGLP6BpmtkZAyJGB513ebO78rM7F8Ht3yBs\nh1RUFigjz6TCR/pItdkkT3urBjuQkTNvBaFZLfqtrxkbs/X9jNwHruzVrmECWTUO\nolG3Ub0hNc6buoDTI4fXVbim89FOH3/upO7Ptd3NfO3yxeBLESRt3yv8mwXBpBU+\n4lAgVKGOtc9/HgIPPXlw8VX89WYobObbwDSo8D/V2/sDLIxd26NoVbbPCqpZA10M\nqdfVLq4Sc+yqpl99IWmkGNYUd5pdAYtocwJH6x4KSyE3FOFCf+g0+0o80KJ16fov\nCOBQ57jxCaRggtI/HVlObs/JURSZTHkhfVAOc9OKcQKBgQDqF9haOaw7Nh6GKmgW\n8KW+td/NpnfO+ZORysFZtfvmUp6/6wn2U9FEJZdWhBJW1LVtVuJCY99w7rl7bGsj\nk8g2J1QVtbtCxUBsZJTNZKr5nFr2EXAJ3+0+XHUZAggtIVq4iLPhWdTkI5mP+l5+\nAVfbpQONRtnd+QXVy4VYyU9ELwKBgQDT395C84AlTIzfzn0N/CQVHQHhf79MyzdI\nrdBCoy4k3WHqGniWwCbuqFWs53t5EaY6wneh8hnVVE+QiKwPgi5YeR3Pw39lXj/2\njZSP3YaqUbTnPbFr94z3RqF3+9vSpu4AGNfQZcBKWj0AMGd6hnKSU/kG8GuBGkTw\n+ZRbnry8EQKBgQCfqVHT///7hqb9BRFnjAzP7UZPAlo23byLtIl5gYjkh7dk2I87\n5eEWJLl6tau4c22mvJqng2zTns79Ym4UnufwH5TXFdM58EVHaLag/CctBjp4GF6d\nLZCndvIa82rWNSimMf7WFaoBTFKhg7dNI+djlMG+avOP1RfowN4bN3qL2wKBgG4X\n16AmcyHugw0QeL65k+48omuQO9Elj1Z+qsbVj/ar6mMA2kRLGG/OnKY5qlkgqKXD\nwvItoOrO4oER44YzeO2UEb+RsDL2JHpy2w1eaMk7p6q4zeZyPZeH5gM4peLxxp3a\nStoI5UA9X5Enlb1++y254J6QcuwkwEoPBd4Nv7hhAoGAUsDfEeogFPcgFUOtlxYW\nYPghvn0WyaXhOZT3wk/BYR5LHDUHHml4ScfzUvJjxw7m5g13LLQTpQ/lja7JBby6\nu6StRiPfKUdxmI2Kie8KyQOd+QMck+HzziA19TmKuZivAL3qufd+D6G/4J9p8gU6\nawpbjvAsE23b7EsooJzCnm0=\n-----END PRIVATE KEY-----\n",
    "client_email": "mrgorkiy@alert-synapse-375418.iam.gserviceaccount.com",
    "client_id": "115320844447310273299",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mrgorkiy%40alert-synapse-375418.iam.gserviceaccount.com"
}
# pprint(INFO)
cred = ServiceAccountCreds(scopes=SCOPES, **INFO)


async def get_service():
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
