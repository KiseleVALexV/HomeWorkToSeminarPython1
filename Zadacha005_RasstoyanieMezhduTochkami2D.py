# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
x1=float(input('введите координату х первой точки :'))
y1=float(input('введите координату y первой точки :'))
x2=float(input('введите координату х второй точки :'))
y2=float(input('введите координату y второй точки :'))
dist=((x2-x1)**2+(y2-y1)**2)**0.5
print('расстояние между точками : ', dist)
