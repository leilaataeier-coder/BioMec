import numpy

def угол(а, б, в):
    первая = а - б
    вторая = в - б
    косинус = numpy.dot(первая, вторая) / (numpy.linalg.norm(первая)*numpy.linalg.norm(вторая))
    return 180 - numpy.degrees(numpy.arccos(numpy.clip(косинус, -1, 1)))

а = numpy.array([156.76045627, 262.40304183])
б = numpy.array([135.81047500, 295.78161451])
в = numpy.array([182.59268596, 271.91367590])
генератор = numpy.random.default_rng(2024)
углы = []
for номер in range(10000):
    аа = а + генератор.normal(0, 1, 2)
    бб = б + генератор.normal(0, 1, 2)
    вв = в + генератор.normal(0, 1, 2)
    углы.append(угол(аа, бб, вв))

центр = sum(углы) / len(углы)
дисперсия = sum((значение-центр)**2 for значение in углы) / (len(углы)-1)
print('исходный угол:', round(угол(а, б, в), 3))
print('средний угол:', round(центр, 3))
print('дисперсия угла:', round(дисперсия, 3))
print('стандартное отклонение:', round(дисперсия**0.5, 3))
