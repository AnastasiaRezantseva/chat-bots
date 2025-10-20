from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def can_handle(self, update: dict) -> bool: ...
    def handle(self, update: dict) -> bool:
        """
        return options:
        - true - signal for dispatcher to continue processing
        - false - signal for dispatcher to STOP processing
        """
        pass 
