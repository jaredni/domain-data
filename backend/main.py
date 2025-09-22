from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schema import RequestSchema, DomainInformationSchema, ContactInformationSchema, DataTypeEnum, ResultsSchema
from connector import WhoIs

app = FastAPI()
# Allow all origins, all methods, and all headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.post("/domain-data")
async def fetch_domain_data(data: RequestSchema):
    domain = data.domain_name
    data_type = data.data_type

    whois = WhoIs()

    results = whois.who_is_service_post(domain)

    if "error" in results:
        return results

    results_data = dict()

    results_data["data"] = results["WhoisRecord"]
    results_data["data"]["information_type"] = data_type

    return ResultsSchema(**results_data).model_dump()

