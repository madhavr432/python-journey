from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional

class Patient(BaseModel):

    name : str
    age : int
    email: EmailStr
    weight : float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]
    emergency: Optional[int] = None

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("patients older than 60 must have an emergency contact")
        return model
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {'name': 'nitish', 'age': 90, "email": "abc@gmail.com", 'weight': 75.43, 'married': True, "allergies": ["nuts", "honey"], "contact_details": { "phone": "99391144555",'emergency': '5624852'}}

patient = Patient(**patient_info)


update_patient_data(patient)