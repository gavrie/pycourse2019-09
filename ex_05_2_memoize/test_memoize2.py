from typing import Dict

num_calls: Dict[str, int] = {}


def fetch_stars(repo: str) -> None:
    print(f"Fetching stars for {repo}")
    num_calls[repo] = num_calls.get(repo, 0) + 1


def test_cached_fetch():
    assert num_calls == {}
    redis = "antirez/redis"
    hazel = "hazelcast/hazelcast"

    fetch_stars(redis)
    assert num_calls == {redis: 1}

    fetch_stars(hazel)
    assert num_calls == {redis: 1, hazel: 1}

    fetch_stars(redis)
    assert num_calls[redis] == 2
