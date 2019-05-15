最小二乗法
===

# 1. 今回の目的

データの集合を点で表すとき、その点同士を関数で近似すると、他の点を予測したりすることができます。
今回は、データから一次関数で近似を行う最小二乗法を学び、実装してみます。

# 2. 最小二乗法とは

最小二乗法、特に今回扱う1次の最小二乗法についてです。
これは、任意のデータの集合を一次関数で近似する手法となります。

まず、近似式を以下のように表現します。

$y = ax + b$

そして、与えられたN個のデータを当てはめます。



そうすると、本来当初の式で出るはずだったyとの誤差が求まります。
n個目のデータの誤差を$g_n$とすると、以下のようになるはずです。

$g_1 = y_1 - (ax_1 + b)$
$g_2 = y_2 - (ax_2 + b)$
$g_3 = y_3 - (ax_3 + b)$
︙
$g_n = y_n - (ax_n + b)$

データの絶対値を取ることは難しいため、2乗することで負の数の誤差も値として使えるようにします。
そうして、すべての誤差を足すと、誤差の合計が求まりました。
誤差の合計を$g$と表すとき、以下のように表現できます。

$g = \frac{1}{2} \sum_{n=1}^{N} (g_n)^2$

※1/2をかけているのは計算を簡単にするため

このgが最小になるような、aとbを見つけます。

方法は簡単で、aとbでそれぞれ偏微分することでaとbを求められます。

計算を効率よくするために、行列式で表すと、以下のようになります。

$\begin{pmatrix}
\sum_{N}^{n=1} (x_n)^2 & \sum_{N}^{n=1} (x_n) \\
\sum_{N}^{n=1} (x_n)   & \sum_{N}^{n=1} 1 \\
\end{pmatrix}
=\begin{pmatrix}
a \\
b \\
\end{pmatrix}\begin{pmatrix}
\sum_{N}^{n=1} (x_n)(y_n) \\
\sum_{N}^{n=1} (y_n) \\
\end{pmatrix}$

# 3. 実装

今回は、すでにある程度完成したコードがあるため、そこから追加する形で実装しました。
コードの差分は以下です。

```diff
diff --git a/lsm.c b/lsm.c
index b041432..7edada9 100644
--- a/lsm.c
+++ b/lsm.c
@@ -40,15 +40,44 @@ void dispData(struct dataset data[], int dataNumber)

 void lsm(struct dataset data[], int dataNumber)
 {
+  int i;
+  double xsum =0;
+  double dxsum =0;
+  double ysum =0;
+  double xysum =0;
+
   dispData(data, dataNumber);

   printf("\n");
-  printf("(%lf, %lf)\n", data[0].x, data[0].y);
-  printf("(%lf, %lf)\n", data[1].x, data[1].y);
-  printf("(%lf, %lf)\n", data[2].x, data[2].y);

-
+  for(i=0; i<dataNumber; i++) {
+    xsum += data[i].x;
+  }
+
+  for(i=0; i<dataNumber; i++) {
+    dxsum += data[i].x * data[i].x;
+  }
+
+  for(i=0; i<dataNumber; i++) {
+    xysum += data[i].x * data[i].y;
+  }
+  for(i=0; i<dataNumber; i++) {
+    ysum += data[i].y;
+  }
+
+  double under = (dxsum * dataNumber) - (xsum * xsum);
+
+  //double a = dxsum * xysum + xsum * ysum;
+  double a = dataNumber * xysum + -xsum * ysum;
+  //double b = xsum * xysum + dataNumber * ysum;
+  double b = -xsum * xysum + dxsum * ysum;
+
+  double aa = a / under;
+  double bb = b / under;

+  printf("(%lf %lf)(a) = (%lf)\n",dxsum,xsum,xysum);
+  printf("(%lf %d)(b) = (%lf)\n",xsum,dataNumber,ysum);
+  printf("\n%lf %lf\n",aa,bb);
 }
```

# 4. 演習課題

## 問題1.
aは`1.230769`、bは`3.153846`になりました。

## 問題2.

>ある実験によると、果実Aの直径と水分含有率にある関係があった。
直径5.7cm、6.5cmの果実の果実の水分含有率を推定せよ。


この場合、aは`-6.033835`、bは`-5.011278`となりました。
これを式にすると以下のようになります。

$y = 6.033835x - 5.011278

なので、推定される水分含有率は`29.3815815%`と`34.2086495%`になります。

## 問題3.

aは`0.774297`、bは`0.845697`になりました。

## 問題4.

aは`1.166297`、bは`-2.094569`になりました。