# - - - - - - - - - -

# Что это за проект:

# Здесь находится функция n-ого простого числа (далее "P" функция).
# Я представил P функцию в следующих форматах: чистая математическая нотация, функция в системе Wolfram Mathematica, а также Python функция.
# Все предложенные представления P - отображение одного и того же ресурсоемкого, но рабочего алгоритма, изначально реализованного в чистой математике (поэтому он такой тяжелый).
# В ./draft.txt находятся черновичные данные. Это задел на будущие обновления репозитория.



# - - - - - - - - - -     ∑

# Чистая математика:

# Запись функции:
# 
#   P(n) = 2•([[n-1]-0.5]-[n-1]+0.5)+3•([[n-2]-0.5]-[n-2]+0.5)+∑({a, 5, 2^(n+2)}, a•([[∑({b, 3, a}, [[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]-0.5]-[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]+0.5)+1-n]-0.5]-[∑({b, 3, a}, [[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]-0.5]-[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]+0.5)+1-n]+0.5)•([[∑({b, 3, a-1}, [[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]-0.5]-[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]+0.5)+1-n+1]-0.5]-[∑({b, 3, a-1}, [[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]-0.5]-[∑({c, 2, b-1}, [1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π))]+1-2•b•(0.25-ArcSin(Sin(π/2+2•π•b/c))/(2•π)))/2]+0.5)+1-n+1]+0.5))
#
# Внимание:
# 
#   Cимволы "[" и "]" - обозначение модуля (абсолютного значения) числа взамен традиционным "||". Иначе выражение нельзя было бы прочитать однозначно.
#   Сумма ряда (∑) имеет следующий синтаксис: ∑({varriable, start, end}, expression).



# - - - - - - - - - -

# Wolfram Mathematica:

# Запись функции:
# 
#   P[n_]:=2*(Abs[Abs[n-1]-0.5]-Abs[n-1]+0.5)+3*(Abs[Abs[n-2]-0.5]-Abs[n-2]+0.5)+Sum[a*(Abs[Abs[Sum[Abs[Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]-0.5]-Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]+0.5, {b, 3, a}]+1-n]-0.5]-Abs[Sum[Abs[Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]-0.5]-Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]+0.5, {b, 3, a}]+1-n]+0.5)*(Abs[Abs[Sum[Abs[Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]-0.5]-Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]+0.5, {b, 3, a-1}]+1-n+1]-0.5]-Abs[Sum[Abs[Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]-0.5]-Abs[Sum[Abs[1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi))]+1-2*c*(0.25-ArcSin[Sin[Pi/2+2*Pi*b/c]]/(2*Pi)), {c, 2, b-1}]/2]+0.5, {b, 3, a-1}]+1-n+1]+0.5), {a, 5, 2^(n+2)}]
# 
# Бесплатно протестировать можно здесь: https://www.wolframcloud.com/
# Запускайте функцию на значениях 1, 2, 3, 4, 5 - но не более. Для больших индексов сервис отказывается совершать такие емкие вычисления.



# - - - - - - - - - -

# Python:

import math

def P (n):  # Хорошо работает для n = 1, 2, 3, 4, 5, 6. При больших числах работает слишком долго.

    Abs = lambda n: abs (n)
    Sin = lambda n: math.sin (n)
    ArcSin = lambda n: math.asin (n)
    pi = math.pi

    nth_prime_number = 2*(Abs(Abs(n-1)-0.5)-Abs(n-1)+0.5)+3*(Abs(Abs(n-2)-0.5)-Abs(n-2)+0.5)+sum(a*(Abs(Abs(sum(Abs(Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)-0.5)-Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)+0.5 for b in range (3, a+1))+1-n)-0.5)-Abs(sum(Abs(Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)-0.5)-Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)+0.5 for b in range (3, a+1))+1-n)+0.5)*(Abs(Abs(sum(Abs(Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)-0.5)-Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)+0.5 for b in range (3, a-1+1))+1-n+1)-0.5)-Abs(sum(Abs(Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)-0.5)-Abs(sum(Abs(1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)))+1-2*b*(0.25-ArcSin(Sin(pi/2+2*pi*b/c))/(2*pi)) for c in range (2, b-1+1))/2)+0.5 for b in range (3, a-1+1))+1-n+1)+0.5) for a in range (5, 2**(n+2)+1))

    return int (nth_prime_number)

print (P (7))  # Вставьте любое натуральное число.