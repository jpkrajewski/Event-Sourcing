from uuid import UUID
from typing import Dict
from blockchains.dataclasses import Block


class BlockChain:
    def __init__(self) -> None:
        self.blocks: Dict[UUID, Block] = {}

    def add_block(self, block: Block):
        uuid = block.transaction.from_uuid
        if uuid not in self.blocks:
            self.blocks[uuid] = block
        else:
            prev_block = self.blocks[uuid]
            block.prev = prev_block
            self.blocks[uuid] = block
