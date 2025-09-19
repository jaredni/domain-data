from fastapi import FastAPI

from schema import RequestSchema, DomainInformationSchema, ContactInformationSchema, DataTypeEnum
from connector import WhoIs

app = FastAPI()


@app.post("/domain-data")
async def fetch_domain_data(data: RequestSchema) -> DomainInformationSchema | ContactInformationSchema:
    domain = data.domain_name
    data_type = data.data_type

    whois = WhoIs()

    result = whois.who_is_service_post(domain)

    if data_type == DataTypeEnum.contact_information:
        return ContactInformationSchema(**result["WhoisRecord"])
    elif data_type == DataTypeEnum.domain_information:
        return DomainInformationSchema(**result["WhoisRecord"])
    else: 
        raise ValueError("Invalid data type")

