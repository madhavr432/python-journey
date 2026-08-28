from pydantic import BaseModel,EmailStr, AnyUrl, Field
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length = 50, title = "Name of the patient", description="Give the name of the patient in less than 50 chars", examples=["mohan","amit"])]
    age : int = Field(gt=18,lt = 60)
    email: EmailStr
    website: AnyUrl
    weight : Annotated[float, Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default= None)]
    allergies : Optional[List[str]] = None
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.website)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.website)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info1 = {'name': 'nitish', 'age': 30, "email": "abc@gmail.com","website": "https://amazon.in", 'weight': 75.43, 'married': True, "allergies": ["nuts", "honey"], "contact_details": { "phone": "99391144555"}}

patient_info2 = {'name': 'manish', 'age': 28,"email": "alpha@gmail.com","website": "https://flipkart.in", 'weight': 69.69, "contact_details": { "phone": "6262172262"}}

patient1 = Patient(**patient_info1)

patient2 = Patient(**patient_info2)

insert_patient_data(patient1)
update_patient_data(patient2)