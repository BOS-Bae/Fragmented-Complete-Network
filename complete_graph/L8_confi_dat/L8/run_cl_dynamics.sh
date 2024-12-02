#!/bin/bash

MCS=$1
condi=$2
ns=$3

N=50

for ((i=0; i<$ns; i++))
do
		./cluster_dynamics $N $MCS $condi >> ./dat_cluster_L8/N$N-$1MCS-condi$2.dat
done
