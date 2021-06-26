
from multiprocessing import Manager
from multiprocessing.managers import BaseManager


class MultiProcessingSharedObject:
    """ Returns a complex-object of custom class type, implementing a proxy between dedicated memory areas, able to be safely shared between Processes and Threads """

    @staticmethod
    def create(class_type: type):

        # Start multiprocessing managers
        BaseManager.register(class_type.__name__, class_type)
        manager = BaseManager()
        manager.start()

        # Retrieve the callable of the instance for the class type
        instance_callable = getattr(manager, class_type.__name__)
        return instance_callable()


class A():
    def __init__(self) -> None:
        self.a = 2


BaseManager.register('A', A)
manager = BaseManager()
manager.start()

# Retrieve the callable of the instance for the class type
a = manager.A()


x = 2

# instance = MultiProcessingSharedObject.create(A)
# print(instance.a)
