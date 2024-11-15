#!/bin/bash

N=$1
cidx=$2
./number_show.sh $N $cidx > ./flip_dat/uni-N$N-L8-idx$cidx.dat
python3 prob_cal.py $N $cidx > ./flip_dat/prob-N$N-L8-idx$cidx.dat
./mat_show $N $cidx
