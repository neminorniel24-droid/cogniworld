"""
Lightweight episodic memory: each agent keeps its last N events as plain
Python objects (not GPU tensors -- this is small, infrequent, and CPU-side
by nature). This stands in for ChromaDB/Redis until the project genuinely
needs vector similarity search or persistence across runs.
"""
from collections import deque

MEMORY_LEN = 12


class MemoryStore:
    def __init__(self, n_agents: int):
        self.buffers = [deque(maxlen=MEMORY_LEN) for _ in range(n_agents)]

    def log(self, idx: int, step: int, event: str):
        self.buffers[idx].append({"step": step, "event": event})

    def log_many(self, indices, step: int, event: str):
        for idx in indices:
            self.log(int(idx), step, event)

    def get(self, idx: int):
        return list(self.buffers[idx])

    def resize_slot(self, idx: int):
        """Clear memory when an agent slot is reused for a new offspring."""
        self.buffers[idx].clear()
