import datetime
from typing import Optional

from sqlalchemy import and_, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
            self,
            *,
            from_reserve: datetime,
            to_reserve: datetime,
            meetingroom_id: int,
            reservation_id: Optional[int] = None,
            session: AsyncSession
    ) -> list[Reservation]:
        select_stmt = select(self.model).where(
            self.model.meetingroom_id == meetingroom_id,
            and_(
                self.model.from_reserve <= to_reserve,
                self.model.to_reserve >= from_reserve
            )
        )
        if reservation_id is not None:
            select_stmt = select_stmt.where(
                self.model.id != reservation_id
            )
        reservations = await session.execute(select_stmt)
        return reservations.scalars().all()

    async def get_future_reservations_for_room(
            self, room_id: int, session: AsyncSession
    ) -> list[Reservation]:
        reservations = await session.execute(
            select(self.model).where(
                self.model.meetingroom_id == room_id,
                self.model.to_reserve > datetime.datetime.now()
            )
        )
        return reservations.scalars().all()

    async def get_by_user(
            self, user_id: int, session: AsyncSession
    ) -> list[Reservation]:
        reservations = await session.execute(
            select(self.model).where(
                self.model.user_id == user_id,
                self.model.to_reserve > datetime.datetime.now()
            )
        )
        return reservations.scalars().all()

    async def get_count_res_at_the_same_time(
            self,
            from_reserve: datetime,
            to_reserve: datetime,
            session: AsyncSession
    ) -> list[dict[str, int]]:
        reservations = await session.execute(
            select([Reservation.meetingroom_id,
                    func.count(Reservation.meetingroom_id)]).where(
                Reservation.from_reserve >= from_reserve,
                Reservation.to_reserve <= to_reserve
            ).group_by(Reservation.meetingroom_id)
        )
        return reservations.all()


reservation_crud = CRUDReservation(Reservation)
