from typing import Any

import humps
import requests

class SwitchBotClient(requests.Session):

    API_ROOT = 'https://api.switch-bot.com'
    API_VERSION = 'v1.0'

    def __init__(self, token: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.headers['Authorization'] = token

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        url = '/'.join([self.API_ROOT, self.API_VERSION, path.strip('/')])
        response = super().request(method, url, **kwargs)

        # Raise an exception for non-successful status codes.
        response.raise_for_status()

        json_response = humps.decamelize(response.json())

        # Check the returned status_code in the payload and raise an error for
        # anything other than 100 (success).
        status_code = json_response['status_code']
        if status_code != 100:
            raise RuntimeError(
                f'The SwitchBot API returned an unsuccessful status code {status_code}:'
                f'{json_response["message"]}')

        return json_response
