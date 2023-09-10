from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.endpoints.validators import (check_meeting_room_exists,
                                          check_reservation_before_edit,
                                          check_reservation_intersections)
from app.core.db import get_async_session
from app.crud.reservation import reservation_crud
from app.schemas.reservation import (ReservationCreate, ReservationDb,
                                     ReservationUpdate)
from app.core.user import current_user, current_superuser
from app.models import User

router = APIRouter()


@router.post('/', response_model=ReservationDb)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(
        **reservation.dict(), session=session
    )
    new_reservation = await reservation_crud.create(
        reservation, session, user
    )
    return new_reservation


@router.get(
        '/',
        response_model=list[ReservationDb],
        dependencies=[Depends(current_superuser)]
)
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров."""
    reservations = await reservation_crud.get_multi(session)
    return reservations


@router.get(
        '/my_reservations',
        response_model=list[ReservationDb],
        response_model_exclude={'user_id'}
)
async def get_my_reservations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Получает список всех бронирований для текущего пользователя."""
    reservations = await reservation_crud.get_by_user(user.id, session)
    return reservations


@router.delete('/{reservation_id}', response_model=ReservationDb)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Для суперюзеров или создателей объекта бронирования."""
    reservation = await check_reservation_before_edit(
        user, reservation_id, session
    )
    reservation = await reservation_crud.remove(reservation, session)
    return reservation


@router.patch(
        '/{reservation_id}',
        response_model=ReservationDb
)
async def update_reservation(
    reservation_id: int,
    obj_in: ReservationUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Для суперюзеров или создателей объекта бронирования."""
    reservation = await check_reservation_before_edit(
        user, reservation_id, session
    )
    await check_reservation_intersections(
        **obj_in.dict(),
        reservation_id=reservation_id,
        meetingroom_id=reservation.meetingroom_id,
        session=session
    )
    reservation = await reservation_crud.update(reservation, obj_in, session)
    return reservation
