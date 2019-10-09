from abc import ABCMeta, abstractmethod


class _Rule(metaclass=ABCMeta):
    @abstractmethod
    def valid(self, path):
        pass
