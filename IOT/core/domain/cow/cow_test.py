import uuid
from core.domain.cow.cow import Cow
from core.domain.common.value_objects.timestamp import TimeStamp


def test_instance():
    cow = Cow(
        cow_id=str(uuid.uuid4()),
        name="Bessie",
        cow_birth_date=TimeStamp.now(),
        last_birth_date=TimeStamp.now()
    )
    assert isinstance(cow, Cow) 
   

def test_to_dict():    
    cow = Cow(
        cow_id=str(uuid.uuid4()),
        name="Bessie",
        cow_birth_date=TimeStamp.now(),
        last_birth_date=TimeStamp.now()
    )   
    cow_dict = cow.to_dict()
    assert isinstance(cow_dict, dict)
    assert cow_dict["cow_id"] == cow.cow_id
    assert cow_dict["name"] == cow.name
    assert cow_dict["cow_birth_date"] == cow.cow_birth_date.value.isoformat()
    assert cow_dict["last_birth_date"] == cow.last_birth_date.value.isoformat()