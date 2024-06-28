#!/bin/bash

M=$1
N=0
L=$((M+M-1))
for ((i=1; i<=$M; i++))
	do
		N=$((N+i))	
	done

echo $L
