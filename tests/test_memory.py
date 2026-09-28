from memory.store import MemoryStore, MEMORY_LEN


def test_log_appends_event():
    store = MemoryStore(n_agents=3)
    store.log(0, step=5, event="ate food")
    assert store.get(0) == [{"step": 5, "event": "ate food"}]
    assert store.get(1) == []  # other agents untouched


def test_ring_buffer_caps_at_memory_len():
    store = MemoryStore(n_agents=1)
    for step in range(MEMORY_LEN + 5):
        store.log(0, step=step, event="tick")
    events = store.get(0)
    assert len(events) == MEMORY_LEN
    # oldest events should have been dropped -- first kept step is offset by
    # however many were pushed out
    assert events[0]["step"] == 5
    assert events[-1]["step"] == MEMORY_LEN + 4


def test_log_many_writes_same_event_to_all_indices():
    store = MemoryStore(n_agents=5)
    store.log_many([1, 3], step=1, event="died")
    assert store.get(1) == [{"step": 1, "event": "died"}]
    assert store.get(3) == [{"step": 1, "event": "died"}]
    assert store.get(0) == []


def test_resize_slot_clears_buffer():
    store = MemoryStore(n_agents=2)
    store.log(0, step=1, event="ate food")
    store.resize_slot(0)
    assert store.get(0) == []
