from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, obj: any):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, ref) -> any:
        raise NotImplementedError

        
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session
    
    def add(self, obj) -> None:
        self.session.add(obj)
    
    def get(self, ref) -> any:
        # return self.session.query(model)
        ...