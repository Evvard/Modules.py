from pydantic import Field, BaseModel, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional
from typing_extensions import Self


class ContactType(Enum):
    radio:
    visual:
    physical:
    telepathic:
    
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)

    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)

    duration_minutes: int = Field(ge=1, le= 1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, le= 500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contact_checker(self) -> Self:
        if self.contact_id.startswith('AC'):
            return self
        raise ValidationError("Contact Id must be start with AC")
    
    


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        alien = AlienContact(
                            contact_id="AC_2024_001",
                            timestamp=
                            contact_type= 
                            location= "Area 51, Nevada",
                            signal_strength=8.5,
                            duration_minutes=45,
                            witness_count=5,
                            message_received="Greetings from Zeta Reticuli"
                            )
        print(f"ID: {alien.contact_id}")
        print(f"Type: {}")
        print(f"Location {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        if isinstance(alien.message_received, str):
            print(f"Message: {alien.message_received}")

    except ValidationError as m:
        print(f"Expected validation error: {m}")
    finally:
        print("\n======================================")







Custom Validation Rules
Implement @model_validator(mode=’after’) with these business rules:
• Contact ID must start with "AC" (Alien Contact)
• Physical contact reports must be verified
• Telepathic contact requires at least 3 witnesses
• Strong signals (> 7.0) should include received messages


if __name__ == "__main__":
    main()
