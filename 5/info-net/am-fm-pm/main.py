#!/usr/bin/python
"""
Copyright (C) 2020 onokatio(おのかちお)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

このプログラムはフリーソフトウェアです。あなたはこれを、フリーソフトウェ
ア財団によって発行された GNU 一般公衆利用許諾契約書(バージョン3か、希
        望によってはそれ以降のバージョンのうちどれか)の定める条件の下で再頒布
または改変することができます。

このプログラムは有用であることを願って頒布されますが、*全くの無保証*
です。商業可能性の保証や特定の目的への適合性は、言外に示されたものも含
め全く存在しません。詳しくはGNU 一般公衆利用許諾契約書をご覧ください。

あなたはこのプログラムと共に、GNU 一般公衆利用許諾契約書の複製物を一部
受け取ったはずです。もし受け取っていなければ、<http://www.gnu.org/licenses/>
を確認してください。
"""

import math
import numpy
import matplotlib.pyplot as plot

def s(t):
    f = 4
    return numpy.cos(2 * math.pi * f * t)

def AM(t):
    A = 1
    alpha = 1
    fc = 32
    return A * ( alpha * s(t) + 1 ) * numpy.cos(2 * math.pi * fc * t)

t = numpy.arange(0,10,0.01)
print(t)
print(s(t))
print(AM(t))

#plot.plot(t,s(t))
#plot.plot(t,AM(t))
r = numpy.fft.fft(AM(t))
plot.plot(numpy.arange(len(r)),numpy.abs(r))
plot.show()
