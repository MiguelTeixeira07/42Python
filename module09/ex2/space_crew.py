from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class SpaceMission(BaseModel):
    class CrewMember(BaseModel):
        member_id: str = Field(min_length=3, max_length=10)
        name: str = Field(min_length=2, max_length=50)
        rank: Rank
        age: int = Field(ge=18, le=80)
        specialization: str = Field(min_length=3, max_length=30)
        years_experience: int = Field(ge=0, le=50)
        is_active: bool = Field(default=True)

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validator(self) -> SpaceMission:
        if self.mission_id[0] != 'M':
            print('Mission ID must start with "M"')

        if not (Rank.COMMANDER in self.crew or Rank.CAPTAIN in self.crew):
            print('Mission must have at least one Commander or Captain')

        expd = [member for member in self.crew if member.years_experience > 4]
        if len(expd) < (len(self.crew) / 2) and self.duration_days > 365:
            print('Long missions (> 365 days) need ', end='')
            print('50%% experienced crew (5+ years)')

        if not all(member.is_active for member in self.crew):
            print('All crew members must be active')

        return self


def main() -> None:
    print('Space Mission Crew Validation')
    print('=========================================')

    mission = SpaceMission(
        mission_id='M2024_MARS',
        mission_name='Mars Colony Establishment',
        destination='Mars',
        launch_date=datetime.now(),
        duration_days=900,
        budget_millions=2500.0,

        crew=[
            SpaceMission.CrewMember(
                member_id='Sarah',
                name='Sarah Connor',
                rank=Rank.COMMANDER,
                age=67,
                specialization='Mission Command',
                years_experience=34,
            ),

            SpaceMission.CrewMember(
                member_id='John',
                name='John Smith',
                rank=Rank.LIEUTENANT,
                age=67,
                specialization='Navigation',
                years_experience=34,
            ),

            SpaceMission.CrewMember(
                member_id='Alice',
                name='Alice Johnson',
                rank=Rank.OFFICER,
                age=67,
                specialization='Engineering',
                years_experience=34,
            )
        ],
    )

    print('Valid mission created:')
    print(f'Mission: {mission.mission_name}')
    print(f'ID: {mission.mission_id}')
    print(f'Destination: {mission.destination}')
    print(f'Duration: {mission.duration_days} days')
    print(f'Budget: ${mission.budget_millions:.1f}M')
    print(f'Crew size: {len(mission.crew)}')
    for member in mission.crew:
        print(f'- {member.name} ({member.rank}) - {member.specialization}')

    print('\n=========================================')
    print('Expected validation error:')

    _ = SpaceMission(
        mission_id='M2024_MARS',
        mission_name='Mars Colony Establishment',
        destination='Mars',
        launch_date=datetime.now(),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            SpaceMission.CrewMember(
                member_id='John',
                name='John Smith',
                rank=Rank.LIEUTENANT,
                age=67,
                specialization='Navigation',
                years_experience=34,
            ),
            SpaceMission.CrewMember(
                member_id='Alice',
                name='Alice Johnson',
                rank=Rank.OFFICER,
                age=67,
                specialization='Engineering',
                years_experience=34,
            )
        ],
    )


if __name__ == '__main__':
    main()
