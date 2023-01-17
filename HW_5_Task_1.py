from os import system


system ( "cls" )

# Напишите программу, удаляющую из текста все слова, содержащие "абв".
test_string = 'АБВ, ылоажы фыыдлх абв? Зщышф вабвв ффлжв абВ'

separators = [ ",", "!", ".", "?" ]

clear_string = " ".join( map( lambda s: s if "абв" not in s.lower() else s[-1] if s[-1] in separators else "", test_string.split() ) ).replace("  ", " ").strip()


print ( "Программа, удаляющую из текста все слова, содержащие фрагмент \"абв\", в любом регистре.\n" )
print( f"{test_string = }" )
print( f"{clear_string = }\n" )
