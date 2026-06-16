from pydantic import BaseModel, EmailStr, Field, ConfigDict


class GeoSchema(BaseModel):
    lat: str 
    lng: str


class AddressSchema(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoSchema


class CompanySchema(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserSchema(BaseModel):
    id: int = Field(ge=0)
    name: str
    username: str
    email: EmailStr
    address: AddressSchema
    phone: str
    website: str
    company: CompanySchema


    model_config = ConfigDict(extra="forbid")