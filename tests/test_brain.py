import torch

from brain.batched_brain import BatchedBrain

DEVICE = torch.device("cpu")


def make_brain(n=6, n_sensors=8, hidden=4, n_actions=4):
    return BatchedBrain(n, n_sensors, hidden, n_actions, DEVICE)


def test_forward_output_shape():
    brain = make_brain(n=6, n_sensors=8, n_actions=4)
    sensors = torch.rand(6, 8)
    out = brain.forward(sensors)
    assert out.shape == (6, 4)


def test_mutate_into_changes_weights_but_stays_close_for_small_std():
    brain = make_brain(n=4)
    src = torch.tensor([0])
    dst = torch.tensor([1])
    original = brain.W1[1].clone()
    brain.mutate_into(src, dst, std=0.01)
    assert not torch.equal(brain.W1[1], original)
    assert not torch.equal(brain.W1[1], brain.W1[0])  # mutation actually applied
    # with tiny std, child should stay close to the parent it copied
    assert torch.allclose(brain.W1[1], brain.W1[0], atol=0.2)


def test_crossover_into_mixes_both_parents():
    brain = make_brain(n=6, n_sensors=8, hidden=16)
    # make parent A and B maximally distinguishable
    brain.W1[0] = torch.zeros_like(brain.W1[0])
    brain.W1[1] = torch.ones_like(brain.W1[1])

    parent_a = torch.tensor([0])
    parent_b = torch.tensor([1])
    dst = torch.tensor([2])
    brain.crossover_into(parent_a, parent_b, dst, std=0.0)  # no mutation noise

    child = brain.W1[2]
    # with std=0, every element must come from exactly parent A (0) or B (1)
    assert torch.all((child == 0) | (child == 1))
    # and, with a big enough tensor, it should actually mix both (not all-0 or all-1)
    assert 0 < child.sum().item() < child.numel()


def test_get_and_set_genome_roundtrip():
    brain = make_brain(n=4)
    idx = torch.tensor([0, 2])
    genome = brain.get_genome(idx)

    other_idx = torch.tensor([1, 3])
    brain.set_genome(other_idx, genome)

    assert torch.equal(brain.W1[1], brain.W1[0])
    assert torch.equal(brain.W1[3], brain.W1[2])
