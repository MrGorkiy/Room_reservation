from datetime import datetime, timedelta

from pydantic import BaseModel, Extra, root_validator, validator, Field

FROM_TIME = (datetime.today() + timedelta(minutes=10)).isoformat(
    timespec='minutes')
TO_TIME = (datetime.today() + timedelta(hours=1)).isoformat(
    timespec='minutes')


class ReservationBase(BaseModel):
    """Базовая модель.
    :param datetime from_reserve: Время начала бронирования переговорки.
    :param datetime to_reserve: Время окончания бронирования переговорки.
    """
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):
    """Схема для полученных данных."""

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationCreate(ReservationUpdate):
    """Схема для полученных данных"""
    meetingroom_id: int


class ReservationDB(ReservationBase):
    """Схема для возвращаемого объекта."""
    id: int
    meetingroom_id: int

    class Config:
        orm_mode = True
