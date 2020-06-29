/*
 *
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

*/

#include <stdio.h>

int main(void){
	double num;
	printf("input x: ");
	scanf("%lf", &num);

	double eps = 0.0000001;
	double a = 1.0 - num;
	while( 1.0 - (a+1.0)*num > eps ){
		a = (1.0-num)*(1.0+a);
		printf("an = %lf\n", a+1.0);
	}
	printf("1/x = %lf\n", a+1.0);
}

