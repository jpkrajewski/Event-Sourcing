from transfers.base_transfer import Transfer
from transactions.dataclasses import Transaction
from transactions.schemas import TRANSACTION_SCHEMA
from transactions.enums import OperationType
from tanks.tank import Tank


class WaterTransfer(Transfer):
    @staticmethod
    def withdraw(tank: Tank, title: str, amount: int) -> Transaction:
        transaction = TRANSACTION_SCHEMA.copy()
        transaction["title"] = title
        transaction["from_uuid"] = tank.get_uuid()
        transaction["amount"] = amount
        transaction["operation"] = OperationType.WITHDRAW
        if not tank.can_pour_out(amount):
            transaction["status"] = False
            transaction[
                "system_message"
            ] = f"ERROR: Can't pour out that volume: {amount}, tank: {tank.get_name()} current {tank.get_amount()} volume."
        else:
            tank.withdraw(amount)
            transaction["status"] = True
            transaction[
                "system_message"
            ] = f"SUCCESS: Poured out volume: {amount}, tank: {tank.get_name()} current volume: {tank.get_amount()}."
        return Transaction(**transaction)

    @staticmethod
    def deposit(tank: Tank, title: str, amount: int) -> Transaction:
        transaction = TRANSACTION_SCHEMA.copy()
        transaction["title"] = title
        transaction["from_uuid"] = tank.get_uuid()
        transaction["amount"] = amount
        transaction["operation"] = OperationType.DEPOSIT
        if not tank.can_pour_in(amount):
            transaction["status"] = False
            transaction[
                "system_message"
            ] = f"ERROR: Can't pour in volume: {amount}, tank: {tank.get_name()} current {tank.get_amount()} volume and max volume {tank.max_volume}."
        else:
            tank.deposit(amount)
            transaction["status"] = True
            transaction[
                "system_message"
            ] = f"SUCCESS: Poured in volume: {amount}, tank: {tank.get_name()} current volume: {tank.get_amount()}."
        return Transaction(**transaction)

    @staticmethod
    def transfer(
        tank_sender: Tank, tank_reciever: Tank, title: str, amount: int
    ) -> Transaction:
        transaction = TRANSACTION_SCHEMA.copy()
        transaction["title"] = title
        transaction["from_uuid"] = tank_sender.get_uuid()
        transaction["to_uuid"] = tank_reciever.get_uuid()
        transaction["amount"] = amount
        transaction["operation"] = OperationType.TRANSFER
        if not tank_reciever.can_pour_in(amount):
            transaction["status"] = False
            transaction[
                "system_message"
            ] = f"ERROR: Can't pour in that volume: {amount}, tank: {tank_reciever.get_name()} current {tank_reciever.get_amount()} volume and max volume {tank_reciever.max_volume}."
            return Transaction(**transaction)
        if not tank_sender.can_pour_out(amount):
            transaction["status"] = False
            transaction[
                "system_message"
            ] = f"ERROR: Can't pour out volume: {amount}, tank: {tank_sender.get_name()} current {tank_sender.get_amount()} volume."
            return Transaction(**transaction)
        tank_sender.transfer(tank_reciever, amount)
        transaction["status"] = True
        transaction[
            "system_message"
        ] = f"SUCCESS: Poured out volume: {amount} from tank: {tank_sender.get_name()} to tank: {tank_reciever.get_name()}."
        return Transaction(**transaction)
