import random
import string
from math import log2


class Rgb:

    def __init__(self, original: list = [], unit: int = 2, avoid=[]):
        self.__unit = unit
        self.__original = original
        self.__original_length = len(original)
        self.__fake_length = (self.__unit - self.__original_length % self.__unit) % self.__unit
        self.__fake_member = []
        for i in range(self.__fake_length):
            self.__fake_member.append(self.random_string(5))
        for member in self.__fake_member:
            self.__original.append(member)
        self.__length = len(self.__original)
        self.__assigned = [pow(2, x) for x in range(self.__length)]
        self.__avoid = avoid
        self.__assigned_avoid = []
        # if

    def __str__(self):
        return """
------
Rgb instance.
Original List: {original}
Assigned: {assigned}
Length: {length}
Fake members: {fake_member}
Fake length: {fake_length}
Avoid: {avoid}
-------
        """.format(
            original=self.original,
            assigned=self.assigned,
            length=self.length,
            fake_member=self.__fake_member,
            fake_length=self.__fake_length,
            avoid=self.avoid
        )

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
    def length(self) -> int:
        return self.__length

    @property
    def assigned(self) -> list:
        return self.__assigned

    @property
    def avoid(self) -> list:
        return self.__avoid

    def encode(self, values: list):
        return [pow(2, self.__original.index(x)) for x in values]

    def decode(self, encoded_list: list):
        return [self.original[int(log2(x))] for x in encoded_list]


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
        material = self.assigned.copy()
        result = []
        while len(material) > 0:
            print(material)
            _group = []
            for i in range(self.__unit):
                _group.append(material.pop(self.get_random_index(material)))

                # todo: Add avoidance validation
            result.append(_group)

        return [self.decode(group) for group in result]

    # def detect_avoid

    @staticmethod
    def random_string(length: int):
        result = ""
        for i in range(length):
            result += random.choice(string.ascii_lowercase)

        return result

    @staticmethod
    def get_random_index(__list=[]):
        return random.randint(0, len(__list) - 1)

