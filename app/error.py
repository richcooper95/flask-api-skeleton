from flask.app import Flask

from typing import Dict, Optional

from . import airlines


class ExternalError(Exception):
    """External-facing error."""
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        payload: Optional[Dict] = None,
    ) -> None:
        self.message = message
        self.payload = payload
        self.status_code = status_code

    def to_dict(self) -> Dict:
        data = dict(self.payload or ())
        data["message"] = self.message

        return data


def register_errorhandlers(app: Flask) -> None:
    airlines.register_errorhandlers(app)
