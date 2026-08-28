from pydantic import BaseModel,EmailStr, AnyUrl, Field,field_validator
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):

    name : str
    age : int
    email: EmailStr
    weight : float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode = 'after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {'name': 'nitish', 'age': 30, "email": "abc@hdfc.com", 'weight': 75.43, 'married': True, "allergies": ["nuts", "honey"], "contact_details": { "phone": "99391144555"}}

patient = Patient(**patient_info)


update_patient_data(patient)