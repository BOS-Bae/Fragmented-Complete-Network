#!/bin/bash

N=$1

./number_show.sh $N > ./flip_dat/uni-N$N-L8-flip-paradise.dat
./mat_show $N 
