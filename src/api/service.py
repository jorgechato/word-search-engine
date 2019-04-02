from api.model import Search
from api.model import Query

from utils.source import get_source
from utils.source import strict_search
from utils.source import flex_search


def _put_to_firebase():
    pass


def _build():
    pass


def search(data):
    model = search_model = Search(
        source=data["source"],
        query=Query(
            strict=data["query"]["strict"],
            word=data["query"]["word"],
            limiters=[] if "limiters" not in data["query"] else data["query"]["limiters"]
        )
    )

    source = get_source(search_model.source)
    if model.query.strict:
        model.set_count(
            strict_search(model.query.word, source)
        )
    else:
        model.set_count(
            flex_search(
                model.query.word,
                model.query.limiters,
                source
            )
        )

    return model
