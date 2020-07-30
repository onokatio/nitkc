#!/usr/bin/python
"""
Copyright (C) 2020 onokatio

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

matrix = [
        [2.0,3.0,4.0,6.0],
        [3.0,5.0,2.0,5.0],
        [4.0,3.0,30.0,32.0],
        ]

matrix = np.array(matrix)
(height, width) = matrix.shape

for i in range(height):
    matrix[i] = matrix[i] / matrix[i][i]
    print(matrix)

    for k in range(i+1,height):
        div = matrix[k][i]
        matrix[k] -= div * matrix[i]
        print(matrix)

print(matrix)

ans = np.zeros(width-1)

#ans[2] = matrix[2][3]
#ans[1] = matrix[1][3] - matrix[1][2] * ans[2]
#ans[0] = matrix[0][3] - matrix[0][2] * ans[2] - matrix[0][1] * ans[1]

#ans[i] = matrix[i][i:-1]

for i in range(height-1,-1,-1):
    ans[i] = matrix[i][width-1] - sum(ans * matrix[i][0:-1])

print(ans)
