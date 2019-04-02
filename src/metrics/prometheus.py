from prometheus_client import Counter
from prometheus_client import Histogram


SEARCH_COUNTER = Counter("search_counter", "number of search")
FLASK_REQUEST_LATENCY = Histogram(
    __name__.replace(".", "_") + "_request_latency_seconds",
    "Flask Request Latency"
)
