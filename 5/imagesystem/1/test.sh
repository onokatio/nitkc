#!/bin/bash

for i in {1..16};do ../bin/diffbmp ./ans$i.bmp ../kadai/no$i/out$i.bmp;done
exit 0
