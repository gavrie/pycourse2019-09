from typing import Dict, Tuple, Any

num_calls: Dict[str, int] = {}


def make_cached(func):
    cache: Dict[Tuple[Any, ...], int] = {}

    def cached(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return cached


@make_cached
def fetch_stars(repo: str) -> int:
    print(f"Fetching stars for {repo}")
    num_calls[repo] = num_calls.get(repo, 0) + 1
    return hash(repo)


def test_cached_fetch():
    assert num_calls == {}
    redis = "antirez/redis"
    hazel = "hazelcast/hazelcast"

    s = fetch_stars(redis)
    assert num_calls == {redis: 1}
    assert s == hash(redis)

    s = fetch_stars(hazel)
    assert num_calls == {redis: 1, hazel: 1}
    assert s == hash(hazel)

    s = fetch_stars(redis)
    assert num_calls[redis] == 1
    assert s == hash(redis)
