import random
import string
from math import log2


class Rgb:

    def __init__(self, original: list = [], unit: int = 2, avoid=[]):
        self.__unit = unit

        self.__original = original.copy()
        self.__original_length = len(self.original)

        self.__material = self.original.copy()

        self.__fake_length = (self.unit - self.length % self.unit) % self.__unit
        self.__fake_member = self.get_fake_members(self.__fake_length)
        for member in self.__fake_member:
            self.__material.append(member)
        self.__material_length = len(self.material)

        self.__assigned = self.assign(len(self.__material))

        self.__assigned_fake_member = self.encode(self.__fake_member)

        self.__avoid = avoid
        self.__compressed_avoid = [self.compress(self.encode(x)) for x in self.avoid]

    def __str__(self):
        return """
------
Rgb instance.
Unit: {unit}
Original List: {original}
Material List: {material}
Assigned: {assigned}
Original Length: {length}
Material Length: {material_length}
Fake members: {fake_member}
Fake length: {fake_length}
Avoid: {avoid}
Assigned Avoid: {assigned_avoid}
-------
        """.format(
            unit=self.unit,
            original=self.original,
            material=self.material,
            assigned=self.assigned,
            length=self.length,
            material_length=self.__material_length,
            fake_member=self.__fake_member,
            fake_length=self.__fake_length,
            avoid=self.avoid,
            assigned_avoid=self.__compressed_avoid
        )

    @property
    def unit(self) -> int:
        return self.__unit

    @unit.setter
    def unit(self, value: int):
        self.__unit = value

    @property
    def original(self) -> list:
        return self.__original

    @original.setter
    def original(self, value: list):
        self.__original = value
        return

    @original.deleter
    def original(self):
        del self.__original

    @property
    def material(self) -> list:
        return self.__material

    @material.setter
    def material(self, value: list):
        self.__material = value
        return

    @material.deleter
    def material(self):
        del self.__material

    @property
    def length(self) -> int:
        return self.__original_length

    @property
    def assigned(self) -> list:
        return self.__assigned

    @property
    def avoid(self) -> list:
        return self.__avoid

    @staticmethod
    def assign(length):
        return [pow(2, x) for x in range(length)]

    def encode(self, values: list):
        return [pow(2, self.__material.index(x)) for x in values]

    def decode(self, encoded_list: list):
        return [self.material[int(log2(x))] for x in encoded_list]

    @staticmethod
    def compress(encoded_list: list):
        return sum(encoded_list)

    @staticmethod
    def decompress(compressed: int):
        decompressed = []
        count = 0
        while compressed is not 0:

            if compressed % 2 is 1:
                decompressed.append(pow(2, count))
            compressed //= 2
            count += 1
        return decompressed

    def build(self):
        is_success = False
        result = []
        while is_success is not True:
            material = self.assigned.copy()
            result = []
            while len(material) > 0:
                _group = []
                for i in range(self.__unit):
                    _group.append(material.pop(self.get_random_index(material)))
                result.append(_group)
            is_success = True

            print(self.__compressed_avoid)
            for group in result:
                print("compress(group) >> {}".format(self.compress(group)))
                if self.compress(group) in self.__compressed_avoid:
                    is_success = False
                    print(group)

        _result = [self.decode(group) for group in result]
        result = []
        for group in _result:
            group = [e if e not in self.__fake_member else "" for e in group]
            result.append(group)

        return result

    @staticmethod
    def random_string(length: int):
        result = ""
        for i in range(length):
            result += random.choice(string.ascii_lowercase)

        return result

    @classmethod
    def get_fake_members(cls, length):
        return [cls.random_string(5) for i in range(length)]

    @staticmethod
    def get_random_index(__list=[]):
        return random.randint(0, len(__list) - 1)
