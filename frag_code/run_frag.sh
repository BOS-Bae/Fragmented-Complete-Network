#!/bin/bash

M=$1
N=0
L=$((M+M-1))
for ((i=1; i<=$M; i++))
	do
		N=$((N+i))	
	done

rule_num=(7 8)
for r in ${rule_num[@]}
	do
	for ((i=0; i<$L; i++))
		do
			./frag_prob $r $i 10000 >> ./result_frag_N$N/L$r/idx$i.dat
		done
	done
