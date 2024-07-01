#!/bin/bash

#this may be useful in the case of using cluster of lab.
M=$1
ns=$2
i=$3
N=0
L=$((M+M-1))
for ((i=1; i<=$M; i++))
	do
		N=$((N+i))	
	done

rule_num=(7 8)

for ((s=0; s<=$ns; s++))
	do
		for r in ${rule_num[@]}
			do
				./frag_prob $r $i 30000 > ./result_frag_N$N/L$r/num_data/idx$i-sample$s.dat
			done
	done
