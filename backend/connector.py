import requests
from config import settings


class WhoIs:
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

        if response.status_code != 200:
            return {"error": "Failed to fetch data from WHOIS service", "status": "error"}

        return response.json()


