from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional as opt


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=.0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_recieved: opt[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator(self) -> 'AlienContact':
        errs = []

        if self.contact_id[:2] != 'AC':
            errs.append('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errs.append('Physical contact must be verified')

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            errs.append('Telepathic contact requires at least 3 witnesses')

        if self.signal_strength > 7.0 and self.message_recieved is None:
            errs.append(
                'Strong signals (> 7.0) should include received messages'
            )

        if errs:
            raise ValueError('\n'.join(errs))

        return self


def main() -> None:
    print('Alien Contact Log Validation')
    print('======================================')
    contact = AlienContact(
        contact_id='AC_2024_001',
        timestamp=datetime.now(),
        location='Area 51, Nevada',
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_recieved='Greetings from Zeta Reticuli'
    )
    print('Valid contact report:')
    print(f'ID: {contact.contact_id}')
    print(f'Type: {contact.contact_type}')
    print(f'Location: {contact.location}')
    print(f'Signal: {contact.signal_strength}/10')
    print(f'Duration: {contact.duration_minutes} minutes')
    print(f'Witnesses: {contact.witness_count}')
    message = contact.message_recieved
    print(f'Message: {message}' if message else '')

    print('\n======================================')
    print('Expected validation error:')
    try:
        _ = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime.now(),
            location='Area 51, Nevada',
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_recieved='Greetings from Zeta Reticuli'
        )
    except ValidationError as e:
        for err in e.errors():
            main_msg = err['msg'].split("('", 1)[0]
            if 'Value error' in main_msg:
                print(main_msg[13:])
            else:
                print(main_msg)


if __name__ == '__main__':
    main()
