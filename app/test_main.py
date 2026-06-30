import time
from unittest import mock

from app.main import can_access_google_page


# def test_can_access_google_page() -> None:
#     current_time = time.strftime("%H")
#     print(current_time)
#     if current_time in range(6, 23):
#         assert can_access_google_page("https://data.rocks") == "Accessible"
#     else:
#         assert can_access_google_page("https://data.rocks") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_with_functions(
        mocked_has_connection: dict,
        mocked_valid_url: dict) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("https://data.rocks") == "Accessible"

    mocked_valid_url.assert_called()
    mocked_has_connection.assert_called()
