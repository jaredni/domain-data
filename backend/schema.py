from enum import Enum
from pydantic import BaseModel, Field, computed_field, PrivateAttr


class DataTypeEnum(str, Enum):
    domain_information = "domain_information"
    contact_information = "contact_information"


class RequestSchema(BaseModel):
    domain_name: str = Field(..., description="Input domain to be processed")
    data_type: DataTypeEnum

    class Config:
        use_enum_values = True


class EstimatedDomainAgeSchema(BaseModel):
    estimated_domain_age: int = Field(..., alias="estimatedDomainAge")


class DomainInformationSchema(BaseModel):
    domain_name: str = Field(..., alias="domainName")
    registrar_name: str = Field(..., alias="registrarName")
    registration_date: str = Field(..., alias="createdDate")
    expiration_date: str = Field(..., alias="expiresDate")
    estimated_domain_age : int = Field(..., alias="estimatedDomainAge")
    name_servers : dict = Field(..., alias="nameServers", exclude=True)

    @computed_field
    def host_names(self) -> list[str]:
        host_names = self.name_servers.get("hostNames", [])

        # truncate host names longer than 25 characters
        return [
            host_name if len(host_name) <= 25 else host_name[:22] + "..."
            for host_name in host_names
        ]


class ContactInformationSchema(BaseModel):
    registrant: dict = Field(..., alias="registrant", exclude=True)
    technical_contact: dict = Field(..., alias="technicalContact", exclude=True)
    contact_email: str = Field(..., alias="contactEmail")

    @computed_field
    def registrant_name(self) -> str:
        return self.registrant.get("name", "N/A")

    @computed_field
    def technical_contact_name(self) -> str:
        return self.technical_contact.get("name", "N/A")

