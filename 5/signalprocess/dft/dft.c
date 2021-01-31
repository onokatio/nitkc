#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
#define N 3/*課題の結果をチェックするためにはこちらは３か4を設定してください*.Sine波の場合は色々変えてみてください*/
#define PI 3.1416
 
struct Values
{
 double Re, Im; 
};

int main()
{
    int n, k;             
    double x[N]={5,2,-2,4};          
    struct Values X[N];
       double frequency1=8;/*1つ目のSine波の周波数*/
    double frequency2=12;/*2つ目のSine波の周波数*/
    int A1=50;/*1つ目のSine波の振幅*/
    int A2=50;/*2つ目ののSine波の振幅*/
    double Magnitude[N];/*フーリエ変換変換後の信号の振幅*/

  for(n=0;n<N;n++)
   {
        double t = (double) n/N;
        x[n] = A1*sin(frequency1*t*2*M_PI)+A2*sin(frequency2*t*2*M_PI); 
    }

//課題の結果をチェック


    for (k=0 ; k<N ; ++k)
    {
        X[k].Re = 0;
        for (n=0 ; n<N ; ++n)
         X[k].Re += x[n] * cos(n * k * 2*PI / N);/*式の通り行列を作ってx(n)と掛け算-----実部*/
         X[k].Im = 0;
        for (n=0 ; n<N ; ++n) 
        X[k].Im -= x[n] * sin(n * k * 2*PI / N);   /*式の通り行列を作ってx(n)と掛け算-----虚部*/
        Magnitude[k]= X[k].Re*X[k].Re+X[k].Im*X[k].Im;
    }
     
    for (k=0 ; k<N ; ++k)
    {
        /*行列の掛け算でデータ結果を表示*/
        if (X[k].Im<0)
        printf ("X[%d]=%.3f%.3fj\n",k,X[k].Re,X[k].Im);
        else
         printf ("X[%d]=%.3f+%.3fj\n",k,X[k].Re,X[k].Im); 
        

    }

    for (k=0 ; k<N ; ++k)
    {
       /* if (X[k].Im<0)
        printf ("X[%d]=%.3f%.3fj\n",k,X[k].Re,X[k].Im);
        else
         printf ("X[%d]=%.3f+%.3fj\n",k,X[k].Re,X[k].Im); */
         printf ("Magnitude[%d]=%.3f\n",k,Magnitude[k]); 

    }
    
}
