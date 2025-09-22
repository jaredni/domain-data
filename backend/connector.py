import requests
from config import settings


class WhoIs:
    """
        A class to interact with the WHOIS service API.
    """
    def who_is_service_post(self, domain_name: str):
        url = f"{settings.WHOIS_API_URL}/WhoisService"

        headers = {
            "Content-Type": "application/json",
        }

        json_data = {
            "domainName": domain_name,
            "apiKey": settings.WHOIS_API_KEY,
            "outputFormat": "JSON"
        }

        response = requests.post(url, headers=headers, json=json_data)

        response_json = response.json()
        data = response_json.get("WhoisRecord", {})

        if not data or data.get("dataError", None):
            return {"error": "Failed to fetch data from WHOIS service", "status": "error"}

        return response_json


