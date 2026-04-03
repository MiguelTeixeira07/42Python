from pydantic import BaseModel, Field, ValidationError
from typing import Optional as opt


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    is_operational: bool = Field(default=True)
    notes: opt[str] = Field(default=None, max_length=200)


def main() -> None:
    print('Space Station Data Validation')
    print('========================================')

    station = SpaceStation(
        station_id='ISS001',
        name='International Space Station',
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3
    )

    print('Valid station created:')
    print(f'ID: {station.station_id}')
    print(f'Name: {station.name}')
    print(f'Crew: {station.crew_size} people')
    print(f'Power: {station.power_level}%')
    print(f'Oxygen: {station.oxygen_level}%')
    print(f'Status: {'' if station.is_operational else 'Not'} Operational')
    print(f'Notes: {station.notes}' if station.notes else '')
    print('========================================')

    print('Expected validation error:')
    try:
        _ = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=67,
            power_level=85.5,
            oxygen_level=92.3
        )
    except ValidationError as e:
        for err in e.errors():
            main_msg = err['msg'].split('(', 1)[0]
            print(main_msg)


if __name__ == '__main__':
    main()
