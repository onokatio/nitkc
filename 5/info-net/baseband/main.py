#!/usr/bin/python

"""
Copyright (c) 2020 onokatio

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
ア財団によって発行された GNU 一般公衆利用許諾契約書(バージョン2か、希
望によってはそれ以降のバージョンのうちどれか)の定める条件の下で再頒布
または改変することができます。

このプログラムは有用であることを願って頒布されますが、*全くの無保証*
です。商業可能性の保証や特定の目的への適合性は、言外に示されたものも含
め全く存在しません。詳しくはGNU 一般公衆利用許諾契約書をご覧ください。

あなたはこのプログラムと共に、GNU 一般公衆利用許諾契約書の複製物を一部
受け取ったはずです。もし受け取っていなければ、<http://www.gnu.org/licenses/>
を確認してください。
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random

data = [random.randrange(0,2) for i in range(1024)]
data = np.reshape(data, (-1, 1) )

def NORMAL(data):
    return data * [1,1,1,1]

def NRZ(data):
    return data * [-1,-1,-1,-1]

def NRZ2(data):
    return data * [-2,-2,-2,-2] + [1,1,1,1]

def RZ(data):
    return data * [0,-1,-1,0]

def RZ2(data):
    return (data * [-1,-1,-1,-1] + [1,1,1,1]) * [0,1,1,0] + RZ(data)

def AMI(data):
    count = []
    invert = 0
    data2 = []
    for index, bit in enumerate(data):
        if bit[0] == 1:
            invert = (invert + 1)%2
            data2.append([1+invert*-2,1+invert*-2,0,0])
        else:
            data2.append([0,0,0,0])
    return np.array(data2)

def MAN(data):
    return (data * [-1,-1,-1,-1] + [1,1,1,1]) * [-1,-1,1,1] + data * [1,1,-1,-1]

def graphdata(data):
    for bits in data:
        for bit in bits:
            if bit:
                print("￣", end="")
            else:
                print("＿", end="")
        print(" ", end="")
    print("")

"""
print(data)
print(NRZ(data))
print(NRZ2(data))
print(RZ(data))
print(RZ2(data))
print(AMI(data))
print(MAN(data))
"""

def plotwave(fig, pos, data, title):
    width = 25
    data = data[0:width+1]
    ax1 = fig.add_subplot(pos)
    ax1.set_title(title)
    ax1.set_xticks(np.arange(0, (width+1)*4, 4), minor=False)
    ax1.set_xticks(np.arange(0, (width+1)*4, 1), minor=True)
    ax1.set_xticklabels(range(width+1))
    ax1.set_axisbelow(False)
    ax1.xaxis.grid(True, 'minor', linestyle='--', zorder=1)
    ax1.xaxis.grid(True, 'major', color='r', zorder=6)
    ax1.plot(np.arange(0, (width+1)*4, 1), data.flatten(), drawstyle='steps-post')
    ax1.set_ylim(-1.1,1.1)
    ax1.set_xlim(0,width*4)
    return ax1

def plotfft(fig, pos, data, title):
    F = np.abs(np.fft.fft(data.flatten()))
    ax = fig.add_subplot(pos)
    ax.plot(range(len(F)), F)
    ax.set_title(title)
    ax.set_ylim(0,300)

fig = plt.figure(tight_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=7, figure=fig)
plotwave(fig, spec[0,0], NORMAL(data), 'data')
plotwave(fig, spec[1,0], NRZ(data), 'NRZ')
plotwave(fig, spec[2,0], NRZ2(data), 'NRZ2')
plotwave(fig, spec[3,0], RZ(data), 'RZ')
plotwave(fig, spec[4,0], RZ2(data), 'RZ2')
plotwave(fig, spec[5,0], AMI(data), 'AMI')
plotwave(fig, spec[6,0], MAN(data), 'MAN')

plotfft(fig, spec[0,1], NORMAL(data), 'data fft')
plotfft(fig, spec[1,1], NRZ(data), 'NRZ fft')
plotfft(fig, spec[2,1], NRZ2(data), 'NRZ2 fft')
plotfft(fig, spec[3,1], RZ(data), 'RZ fft')
plotfft(fig, spec[4,1], RZ2(data), 'RZ2 fft')
plotfft(fig, spec[5,1], AMI(data), 'AMI fft')
plotfft(fig, spec[6,1], MAN(data), 'MAN fft')

plt.show()
