import pytest

from ting_file_management.priority_queue import PriorityQueue


@pytest.fixture  # https://docs.pytest.org/en/latest/explanation/fixtures.html
def priority_queue():
    return PriorityQueue()


def test_basic_priority_queueing(priority_queue):
    first_task = {
        "nome_do_arquivo": "",
        "qtd_linhas": 9,
        "linhas_do_arquivo": [],
    }

    priority_one = {
        "nome_do_arquivo": "",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }

    second_test = {
        "nome_do_arquivo": "",
        "qtd_linhas": 11,
        "linhas_do_arquivo": [],
    }

    priority_two = {
        "nome_do_arquivo": "",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    priority_queue.enqueue(first_task)
    priority_queue.enqueue(priority_one)
    priority_queue.enqueue(second_test)
    priority_queue.enqueue(priority_two)

    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue) == 4

    assert priority_queue.high_priority.search(0) == priority_one
    assert priority_queue.high_priority.search(1) == priority_two
    assert priority_queue.regular_priority.search(0) == first_task
    assert priority_queue.regular_priority.search(1) == second_test

    assert priority_queue.search(1) == priority_two
    assert priority_queue.search(2) == first_task
    assert priority_queue.search(3) == second_test

    assert priority_queue.dequeue() == priority_one
    assert priority_queue.dequeue() == priority_two
    assert priority_queue.dequeue() == first_task
    assert priority_queue.dequeue() == second_test
    assert len(priority_queue) == 0
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(1)
