#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)
    __setattr__ = lambda self, name, value: super().__setattr__(name, value) if hasattr(self, name) or name == 'first_name' else setattr(self, 'first_name', value)

