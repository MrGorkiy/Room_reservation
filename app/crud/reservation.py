from datetime import datetime
from typing import Optional

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Reservation, User


class CRUDReservation(CRUDBase):
    """Класс получения дынных бронирования"""

    @staticmethod
    async def get_reservations_at_the_same_time(
            *,
            meetingroom_id: int,
            from_reserve: datetime,
            to_reserve: datetime,
            reservation_id: Optional[int] = None,
            session: AsyncSession
    ) -> list[Reservation]:
        """Этот метод проверяет, свободен ли запрошенный интервал времени.
        Если это время полностью или частично зарезервировано в каких-то
        объектах бронирования — метод возвращает список этих объектов."""
        select_stmt = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            and_(
                from_reserve <= Reservation.to_reserve,
                to_reserve >= Reservation.from_reserve
            )
        )
        if reservation_id is not None:
            select_stmt = select_stmt.where(Reservation.id != reservation_id)
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    @staticmethod
    async def get_future_reservations_for_room(room_id: int,
                                               session: AsyncSession):
        reservation_room = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == room_id,
                Reservation.to_reserve > datetime.now()
            )
        )
        reservation_room = reservation_room.scalars().all()
        return reservation_room

    @staticmethod
    async def get_by_user(user: User,
                          session: AsyncSession):
        reservation = await session.execute(
            select(Reservation).where(
                Reservation.user_id == user.id
            )
        )
        return reservation.scalars().all()


reservation_crud = CRUDReservation(Reservation)
