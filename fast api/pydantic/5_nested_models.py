from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'dalsingsarai', 'state': 'bihar', 'pin': '848114'}

address = Address(**address_dict)

patient_dict = {'name':'madhav','gender': 'male','age': 19, 'address': address}

patient = Patient(**patient_dict)

print(patient)

print(patient.name)

print(patient.address.city)
