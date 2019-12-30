import pytest

from random_api.common.repository.quotes import get_random_quote, request_quote_api
from random_api.tasks.random_quote import print_random_quote


@pytest.skip
def test_request_quote_api():
    response = request_quote_api()
    assert hasattr(response, "json")
    assert [key in response.json() for key in ["content", "author"]]


@pytest.skip
def test_get_random_quote():
    quote = get_random_quote()
    assert isinstance(quote, str)


@pytest.skip
def test_async_print_random_quote(stub_broker, stub_worker):
    print_random_quote.send()
    stub_broker.join(print_random_quote.queue_name)
    stub_worker.join()
