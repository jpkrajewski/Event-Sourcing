from unittest import mock
from uuid import UUID, uuid5

import pytest

from core.blockchains.blockchain import BlockChain


@pytest.fixture
def blockchain_instance():
    return BlockChain()


@pytest.fixture
def block_instance():
    block = mock.Mock()
    block.transaction.from_uuid = uuid5(namespace=UUID(int=0), name="test")
    return block


def test_add_block_sanity(blockchain_instance, block_instance):
    blockchain_instance.add_block(block_instance)
    assert len(blockchain_instance.blocks) == 1


def test_add_two_blocks_with_same_uuid(blockchain_instance, block_instance):
    blockchain_instance.add_block(block_instance)
    blockchain_instance.add_block(block_instance)
    assert len(blockchain_instance.blocks) == 1


def test_add_two_blocks_with_diffrent_uuids(blockchain_instance, block_instance):
    blockchain_instance.add_block(block_instance)
    block_instance.transaction.from_uuid = uuid5(namespace=UUID(int=0), name="second")
    blockchain_instance.add_block(block_instance)
    assert len(blockchain_instance.blocks) == 2
