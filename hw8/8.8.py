from os import system

word = input('Введите слово\n')
system('espeak --stdout "' + word + '" > task8.wav')
