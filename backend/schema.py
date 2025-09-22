from enum import Enum
from pydantic import BaseModel, Field, computed_field, PrivateAttr
from typing import Literal, Union


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
    information_type: Literal['domain_information']
    domain_name: str = Field(..., alias="domainName")
    registrar_name: str = Field(..., alias="registrarName")
    registration_date: str = Field(..., alias="createdDate")
    expiration_date: str = Field(..., alias="expiresDate")
    estimated_domain_age : int = Field(..., alias="estimatedDomainAge")
    name_servers : dict = Field(..., alias="nameServers", exclude=True)

    @computed_field
    def host_names(self) -> str:
        host_names = self.name_servers.get("hostNames", [])
        host_names_str = ", ".join(host_names)

        if len(host_names_str) > 25:
            return host_names_str[:22] + "..."
        return host_names_str


class ContactInformationSchema(BaseModel):
    information_type: Literal['contact_information']
    registrant: dict = Field(..., alias="registrant", exclude=True)
    technical_contact: dict = Field(..., alias="technicalContact", exclude=True)
    contact_email: str = Field(..., alias="contactEmail")

    @computed_field
    def registrant_name(self) -> str:
        return self.registrant.get("name", "N/A")

    @computed_field
    def technical_contact_name(self) -> str:
        return self.technical_contact.get("name", "N/A")

class ResultsSchema(BaseModel):
    data: Union[ContactInformationSchema, DomainInformationSchema] = Field(discriminator='information_type')

