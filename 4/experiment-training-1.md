実験実習 アセンブラ面接 レポート
===

----

# 基本編

## 1. main関数の戻り値を求めよ

45
## 2. CCRのNとZの意味は？

N:実行結果が負のときは１、Z:実行結果が０のときは１をそれぞれ返す。それら以外の値のときはそれぞれ0を返す。

## 3. r2に3、r3に4が入っているときにmov.w r2,r3を実行した場合、r2、r3それぞれの値は？

r2、r3に3が入る。

## 4. jsr命令の機能は？

プログラムカウンタの内容をリスタートアドレスとしてスタックに退避し、指定された実行アドレスに分岐する。

# 応用編

## 1. r7はどのような役割として使われているか？その意味は？

ここではsp(スタックポインタ)として使われている。スタックの先頭を指している。

## 2. r6はどのような役割として使われているか？その意味は？

ここではfp(フレームポインタ)として使われている。スタックの決まった場所(リターンアドレスなど)を指している。

## 3. rtsの直前ではなにをしているのか？これと直前に対になっている命令がある。その対の役割を図を用いて説明せよ。

rtsの直前では、r6、r7レジスタを操作している。対になっている命令はjsr命令で、rts命令はjsr命令によって呼び出される。

![](https://i.imgur.com/ah8bYKf.jpg)


## 4. rtsが実行される様子を図で示せ。

![](https://i.imgur.com/1sfWz2Z.jpg)