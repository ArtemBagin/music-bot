from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenRequestParams:
    grant_type: str
    code: str
    client_id: str
    client_secret: str

    @classmethod
    def create_authorization_code_flow(
        cls, code: str, client_id: str, client_secret: str
    ) -> TokenRequestParams:
        return cls(
            grant_type="authorization_code",
            code=code,
            client_id=client_id,
            client_secret=client_secret,
        )
