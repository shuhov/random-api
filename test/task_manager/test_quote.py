import pytest

from random_api.common.repository.quotes import get_random_quote, request_quote_api


@pytest.skip
def test_request_quote_api():
    response = request_quote_api()
    assert hasattr(response, "json")
    assert [key in response.json() for key in ["content", "author"]]


@pytest.skip
def test_get_random_quote():
    quote = get_random_quote()
    assert isinstance(quote, str)
