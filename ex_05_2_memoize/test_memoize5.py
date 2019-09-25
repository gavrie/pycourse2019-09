from typing import Dict

num_calls: Dict[str, int] = {}


def fetch_stars(repo: str) -> int:
    print(f"Fetching stars for {repo}")
    num_calls[repo] = num_calls.get(repo, 0) + 1
    return hash(repo)


def make_cached():
    cache: Dict[str, int] = {}

    def cached(repo: str) -> int:
        if repo not in cache:
            cache[repo] = fetch_stars(repo)

        return cache[repo]

    return cached


fetch = make_cached()


def test_cached_fetch():
    assert num_calls == {}
    redis = "antirez/redis"
    hazel = "hazelcast/hazelcast"

    s = fetch(redis)
    assert num_calls == {redis: 1}
    assert s == hash(redis)

    s = fetch(hazel)
    assert num_calls == {redis: 1, hazel: 1}
    assert s == hash(hazel)

    s = fetch(redis)
    assert num_calls[redis] == 1
    assert s == hash(redis)
