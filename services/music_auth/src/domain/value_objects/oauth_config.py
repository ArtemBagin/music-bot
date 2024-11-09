from dataclasses import dataclass


@dataclass
class OAuthConfig:
    client_id: str
    client_secret: str
    oauth_base_url: str
