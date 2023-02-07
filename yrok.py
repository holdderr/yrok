
class UnitOfWork:
    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()

class UserRepository:
    def save(self, obj):
        obj.save()

class BalanceRepository:
    def save(self, obj):
        obj.save()

def make_vip_user():
    unit_of_work = UnitOfWork
    user_repository = UserRepository
    balance_repository = BalanceRepository

    with UnitOfWork() as unit_of_work:
        user_repository.save(user)
        balance_repository.save(balance)
        unit_of_work.commit()

