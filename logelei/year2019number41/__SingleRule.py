from abc import ABCMeta, abstractmethod


class __SingleRule(metaclass=ABCMeta):
    @abstractmethod
    def valid(self, path):
        pass
