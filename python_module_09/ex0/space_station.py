from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 1, 12, 0),
            is_operational=True,
        )
        print("========================================")
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        if valid.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: Not Operational")
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg']}")
        return
    print("\n========================================")
    try:
        invalid = SpaceStation(
            station_id="RSS001",
            name="Russian Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 1, 12, 0),
            is_operational=True,
        )
        print(invalid)
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg']}")
        return


if __name__ == "__main__":
    main()
