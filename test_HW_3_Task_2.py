from os import system
from random import randrange
import unittest


class Tests( unittest.TestCase ):
    def test_equal( self ):
        self.assertEqual( strange_function( [2, 3, 4, 5, 6] ), [12, 15, 16] )
        self.assertEqual( strange_function( [2, 3, 5, 6] ), [12, 15] )
        self.assertEqual( strange_function( [] ), [] )


def strange_function( some_list: list ) -> list:
    some_list_size = len( some_list )
    result_list_size = some_list_size // 2 if some_list_size % 2 == 0 else some_list_size // 2 + 1
    result_list = [some_list[i] * some_list[-i - 1] for i in range( result_list_size )]
    return result_list


def main():
    print("Программа создает список из произведений пар чисел исходного списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n")

    lt = [2, 3, 4, 5, 6]
    print( f"{ lt } -> { strange_function( lt ) }\n" )

    lt = [2, 3, 5, 6]
    print( f"{ lt } -> { strange_function( lt ) }\n" )
    
    # Генератор случайного списка
    new_lt = [randrange(9) + 1 for _ in range(7)]
    print( f"{ new_lt } -> { strange_function( new_lt ) }\n" )

    new_lt.append(randrange(9) + 1)
    print( f"{ new_lt } -> { strange_function( new_lt ) }\n" )



if __name__ == "__main__":
    system( "cls" )

    main()
