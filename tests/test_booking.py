from models.booking import CreateBookingResponse
from src.constant import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соответствует данным: {e}")

    assert parsed.booking.bookingdates.checkin == "2026-01-01"

    assert created_booking["booking"]["firstname"] == BookingData.FIRSTNAME.value, (
        "Вернулось некорректное имя\n"
        f'Response: {created_booking["booking"]["firstname"]}\n'
        f"Ожидаемое имя: {BookingData.FIRSTNAME.value}"
    )
    assert created_booking["booking"]["lastname"] == BookingData.LASTNAME.value, (
        "Вернулась некорректная фамилия\n"
        f'Response: {created_booking["booking"]["lastname"]}\n'
        f"Ожидаемое имя: {BookingData.LASTNAME.value}"
    )


def test_update_booking(
    booking_client, created_booking, auth_token, headers, valid_booking_payload
):
    booking_id = created_booking["bookingid"]
    headers.update({"Cookie": f"token={auth_token}"})
    payload = valid_booking_payload.build()
    payload.update({"firstname": BookingData.UPDATE_FIRSTNAME.value})
    update_response = booking_client.update_booking(booking_id, headers, payload)
    assert update_response.json()["firstname"] == BookingData.UPDATE_FIRSTNAME.value

    print()
    print(update_response.json())
