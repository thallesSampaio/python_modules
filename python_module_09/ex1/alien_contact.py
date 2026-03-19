try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error: Pydantic library is not installed."
          " Please install it using 'pip install pydantic' and try again.")
    exit(1)


from enum import Enum
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)")
        return self

    @model_validator(mode='after')
    def physical_verified(self) -> Self:
        if self.contact_type.value == 3 and \
           self.is_verified is False:
            raise ValueError(
                "Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def telepathic_witness(self) -> Self:
        if self.contact_type.value == 4 and \
           self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode='after')
    def strong_messages(self) -> Self:
        if self.signal_strength > 7.0 and \
           self.message_received is None:
            raise ValidationError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.radio,
            timestamp="2026-03-10",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("======================================")
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.name}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: '{valid.message_received}'\n")
    except ValidationError as e:
        if e.errors()[0]['type'] == 'value_error':
            msg: str = e.errors()[0]['msg'].replace('Value error, ', '')
        else:
            msg = e.errors()[0]['msg']
    print("======================================")
    try:
        valid = AlienContact(
            contact_id="AC_2009_003",
            contact_type=ContactType.telepathic,
            timestamp="2026-03-19",
            location="Capital Wasteland (Mothership of Zeta)",
            signal_strength=8.5,
            duration_minutes=180,
            witness_count=2,
            message_received="War, war never change.",
        )
        print(valid)
    except ValidationError as e:
        if e.errors()[0]['type'] == 'value_error':
            msg: str = e.errors()[0]['msg'].replace('Value error, ', '')
        else:
            msg = e.errors()[0]['msg']
        print(f"Expected validation error:\n{msg}")


if __name__ == "__main__":
    main()
