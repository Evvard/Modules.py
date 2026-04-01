from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print('Space Station Data Validation')
    print('========================================')
    print('Valid station created:')
    try:
        station_s = SpaceStation(
                                station_id="ISS001",
                                name="International Space Station",
                                crew_size=6,
                                power_level=85.5,
                                oxygen_level=92.3,
                                last_maintenance=datetime.now()
                                )
        print(f"ID: {station_s.station_id}")
        print(f"Name: {station_s.name}")
        print(f"Crew: {station_s.crew_size} people")
        print(f"Power: {station_s.power_level}%")
        print(f"Oxygen: {station_s.oxygen_level}%")
        if station_s.is_operational:
            txt = "Operational"
        else:
            txt = "Unoperational"
        print(f"Status: {txt}")
    except ValidationError as m:
        print(f"Unexpected Error: {m}")
    finally:
        print("\n========================================")

    try:
        station_s = SpaceStation(
                        station_id="ISS001",
                        name="International Space Station",
                        crew_size=0,
                        power_level=85.5,
                        oxygen_level=92.3,
                        last_maintenance=datetime.now()
                        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
