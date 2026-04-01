from pydantic import Field, BaseModel, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional
from typing_extensions import Self


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    tele = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)

    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)

    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contact_checker(self) -> Self:
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact Id must be start with AC")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("The contact type is physical and not verified")
        if self.contact_type == ContactType.tele and self.witness_count < 3:
            raise ValueError("If contact is telepatic, it need 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Need a message if your signal is less than 7.0")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        alien = AlienContact(
                            contact_id="AC_2024_001",
                            timestamp=datetime.now(),
                            contact_type=ContactType.physical,
                            location="Area 51, Nevada",
                            signal_strength=8.5,
                            duration_minutes=45,
                            witness_count=5,
                            message_received="'Greetings from Zeta Reticuli'",
                            is_verified=True
                            )
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        if isinstance(alien.message_received, str):
            print(f"Message: {alien.message_received}")

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])
    finally:
        print("\n======================================")

    try:
        alien = AlienContact(
                    contact_id="AC_2024_001",
                    timestamp=datetime.now(),
                    contact_type=ContactType.tele,
                    location="Area 51, Nevada",
                    signal_strength=8.5,
                    duration_minutes=45,
                    witness_count=2,
                    message_received="'Greetings from Zeta Reticuli'",
                    is_verified=True
                    )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
