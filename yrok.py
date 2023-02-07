
def make_transaction(func: callable):
    def transaction_wrapper(*args, **kwargs):
        transaction = db.begin_transaction
        try:
            result = func(*args,**kwargs)
            transaction.commit()
            return result
        except Exception as exc:
            transaction.rollback()
            raise exc

class UserRepository:
    def save(self, obj):
        obj.save()

class BalanceRepository:
    def save(self, obj):
        obj.save()


@transaction
def make_vip_user():

