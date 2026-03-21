try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error: Pydantic library is not installed."
          " Please install it using 'pip install pydantic' and try again.")
    exit(1)


from datetime import datetime
from enum import Enum
from typing import Self


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_time: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        return self

    @model_validator(mode='after')
    def qualified_crew(self) -> Self:
        valid = False
        for r in self.crew:
            if r.rank.value > 3:
                valid = True
        if valid is False:
            raise ValueError("Mission Must have at"
                  " least one Commander or Captain")
        return self

    @model_validator(mode='after')
    def validate_safety_protocols(self) -> Self:
        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            percentage_experienced = (experienced_count / len(self.crew)) * 100
            if percentage_experienced < 50:
                raise ValueError(
                    f"Long missions (> 365 days) need 50% experienced crew. "
                    f"Current: {percentage_experienced:.1f}%")
        return self

    @model_validator(mode='after')
    def active_crew(self) -> Self:
        check = [r for r in self.crew if r.is_active is False]
        if check:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        crew = [
            CrewMember(
                member_id='commander',
                name='Sarah Connor',
                rank=Rank(5),
                age=20,
                specialization='Mission Command',
                years_experience=5,
                is_active=True
            ),
            CrewMember(
                member_id='lieutenant',
                name='John Smith',
                rank=Rank(3),
                age=20,
                specialization='Navigation',
                years_experience=5,
                is_active=True
            ),
            CrewMember(
                member_id='officer',
                name='Alice Johnson',
                rank=Rank(2),
                age=20,
                specialization='Engineering',
                years_experience=5,
                is_active=True
            ),
        ]
    except ValidationError as e:
        print(f"Error: {e.errors()[0]['msg']}")
        exit(1)

    try:
        valid = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_time=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew,
        )
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {valid.mission_name}\n"
              f"ID: {valid.mission_id}\n"
              f"Destination: {valid.destination}\n"
              f"Duration: {valid.duration_days} days\n"
              f"Budget: ${valid.budget_millions}M\n"
              f"Crew size: {len(valid.crew)}")
        print("Crew members:")
        for m in valid.crew:
            print(f"- {m.name} ({m.member_id}) - {m.specialization}")
    except ValidationError as e:
        if e.errors()[0]['type'] == 'value_error':
            msg: str = e.errors()[0]['msg'].replace('Value error, ', '')
        else:
            msg = e.errors()[0]['msg']
        print(f"Expected validation error:\n{msg}")
    print("\n=========================================")
    crew.pop(0)
    try:
        invalid = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_time=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew,
        )
        print(invalid)
    except ValidationError as e:
        if e.errors()[0]['type'] == 'value_error':
            msg: str = e.errors()[0]['msg'].replace('Value error, ', '')
        else:
            msg = e.errors()[0]['msg']
        print(f"Expected validation error:\n{msg}")


if __name__ == '__main__':
    main()
