from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, obj: any):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, ref) -> any:
        raise NotImplementedError


# class StreakSqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session) -> None:
#         self.session = session
    
#     def add(self, obj) -> None:
#         # TODO : require update code
#         self.session.add(obj)
    
#     def get(self, ref) -> any:
#         return 
#         # return self.session.query(Streak).filter_by(reference=ref).one()