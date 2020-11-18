from unittest.mock import patch, MagicMock

from api.api_bitcoin import get_price_for_bitcoin


@patch(
    "api.api_bitcoin.requests.get"
)
def test_get_price_for_bitcoin(mock_get):
    response = MagicMock()
    response.json = MagicMock(return_value = {
        "bpi":{
            "USD":{
                "rate_float":54564
            }
        }
    })

    mock_get.return_value = response

    result = get_price_for_bitcoin()

    assert result == 54564
