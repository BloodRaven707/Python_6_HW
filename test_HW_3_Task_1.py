from os import system
from random import randrange
import unittest


class Tests( unittest.TestCase ):
    def test_equal( self ):
        self.assertEqual( sum( odd_filter( [2, 3, 5, 9, 3] ) ), 12 )
        self.assertEqual( sum( odd_filter( [2, 3, 5, 9, 3, 5, 6, 9, 2, 4] ) ), 30 )


def odd_filter( some_list: list ) -> list:
    return [some_list[i] for i in range( 1, len( some_list ), 2 )]


def format_result_string( some_list: list ) -> str:
    result_string =  f"{ some_list } -> элементы с нечётными индексами: "
    result_string += f"{ odd_filter( some_list[:] ) }, их сумма: "
    result_string += f"{ sum( odd_filter( some_list[:] ) ) }\n"
    return result_string


def main():
    # Task_1. Задайте список из нескольких чисел.
    # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    # Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
    print( "Программа выводит сумму элементов списка, имеющих нечётной индексы.\n" )

    lt = [2, 3, 5, 9, 3]
    print( format_result_string( lt[:] ) )

    [lt.append( randrange( 10 ) ) for _ in range( 5 )]
    print( format_result_string( lt[:] ) )


if __name__ == "__main__":
    system( "cls" )

    main()
