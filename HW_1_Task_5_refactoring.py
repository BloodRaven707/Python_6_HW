from math import sqrt
from functools import reduce
from os import system


class Point:
    def __init__( self,x_init,y_init ):
        self.x = x_init
        self.y = y_init

    def __str__( self ):
        return "".join( [ "Point(", str( self.x ), ", ", str( self.y ), ")" ])


# Как по мне такие вещи нужно променять осознанно, а не где попало, как видно исходный код проще...
def distance( A, B ):
    return reduce( lambda x, y: ( x + y ) ** ( 0.5 ), map( lambda points: ( points[ 1 ] - points[ 0] ) ** 2, zip( [A.x, A.y], [B.x, B.y] ) ) )

    # Исходный код проще, гораздо более читаем, чем лапша из вложенных лямбд, filter, map, zip, enumerate и list comprehension
    # return sqrt( (A.x - B.x) ** 2 + (A.y - B.y) ** 2 )


if __name__ == "__main__":
    system( "cls" )

    print( "\nПрограмма принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.\n" )

    A_x = int( input( "Введите координату точки А по оси Х: " ) )
    A_y = int( input( "Введите координату точки А по оси Y: " ) )
    B_x = int( input( "Введите координату точки B по оси Х: " ) )
    B_y = int( input( "Введите координату точки B по оси Y: " ) )

    A, B = Point( A_x, A_y ), Point( B_x, B_y )
    print( f"\nРасстояние между: { A }; { B } -> {( int( distance( A, B ) * 100 ) / 100 ):.2f}\n" )  # После :.2f нельзя ставить пробель.
