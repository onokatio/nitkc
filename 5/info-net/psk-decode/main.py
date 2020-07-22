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

import numpy as np
import matplotlib.pyplot as plt

A = 1
N = 128

def PSK(data):
    t = np.arange(N)
    fc = 2
    return A * np.cos(2*np.pi*fc*t/N + np.pi * data)

def PSKdw(data):
    t = np.arange(N)
    fc = 2
    return A * np.cos(2*np.pi*fc*t/N)

bits = [0,1,0,1,0,1,0,1,0]
#bits = []

str = ""

while True:
    print("input number or 'q': ", end='')
    string = input()
    if string == 'q':
        break
    bits.append(int(string))

sequence = np.arange(0, len(bits)*128, 128)

wave_psk = []
wave_psk_h = []

for bit,seq  in zip(bits,sequence):
    wave_psk.extend( PSK(bit) )
    wave_psk_h.extend( PSKdw(bit) )


wave_psk = np.array(wave_psk)
wave_psk *= np.array(wave_psk_h)


wave_psk = np.fft.fftshift(np.fft.fft(np.fft.fftshift(wave_psk)))


wave_psk[:512-16] = 0
wave_psk[512+16:] = 0

wave_psk = np.fft.fftshift(np.fft.ifft(np.fft.fftshift(wave_psk)))

plt.plot(np.arange(len(wave_psk)), wave_psk)
plt.show()
