from os import system
from random import random
import unittest


class Tests(unittest.TestCase):
    def test_equal(self):
        self.assertEqual( strange_function( [1.1, 1.2, 3.1, 5, 10.01] ), 0.19 )


def strange_function( some_list: list ) -> float:
    temp = [round( el % 1, 2 ) for el in some_list if el % 1 != 0]
    return round( max( temp ) - min( temp ), 2 )
     


def main():
    print( "Программа ищет разницу между максимальным и минимальным значением дробной части элементов списка.\n" )

    lt = [1.1, 1.2, 3.1, 5, 10.01]
    print( f"{ lt } -> { strange_function( lt[:] ) }\n" )

    # Генератор случайного списка
    new_lt = [round( random() * 100, 2 ) for _ in range(5)]
    print( f"{ new_lt } -> {strange_function( new_lt[:] ):.2f}\n" )


if __name__ == "__main__":
    system( "cls" )

    main()
