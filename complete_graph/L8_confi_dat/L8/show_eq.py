import numpy as np
import sys


if (len(sys.argv) < 2):
	print("python3 show_eq.py m n") 
	exit(1)


m = int(sys.argv[1])
n = int(sys.argv[2])
N = m+n

var_list = []

# for state 1
for k in range(0, n+1):
	for h in range(0,m):
		print("q1{0}{1} == T12*q2{0}{1} + T13*q3{0}{1} + Om({0})*q1{2}{1} + Op({0})*q1{3}{1} + Zm({1})*q1{0}{4} + Zp({1})*q1{0}{5} + (1-(T12 + T13 + Om({0}) + Op({0}) + Zm({1}) + Zp({1}))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q1{0}{1}".format(int(k),int(h)))

# for state 2
for k in range(0, n+1):
	for h in range(0, m):
		print("q2{0}{1} == T21*q1{0}{1} + T23*q3{0}{1} + Om({0})*q2{2}{1} + Op({0})*q2{3}{1} + Xm({1})*q2{0}{4} + Xp({1})*q2{0}{5} + (1-(T21 + T23 + Om({0}) + Op({0}) + Xm({1}) + Xp({1}))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q2{0}{1}".format(int(k),int(h)))

# for state 3
for k in range(0, n+1):
	for h in range(0,m):
		if (k==n and k==m-1):
			print("q3{0}{1} == T31*q1{0}{1} + T32*q2{0}{1} + wm({0})*q3{2}{1} + wp({0})*q3{3}{1} + Xm({1})*q3{0}{4} + Xp({1})*q3{0}{5} + (1-(T31 + T32 + wm({0}) + wp({0}) + Xm({1}) + Xp({1}))*q3{0}{1}, ".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		else:
			print("q3{0}{1} == T31*q1{0}{1} + T32*q2{0}{1} + wm({0})*q3{2}{1} + wp({0})*q3{3}{1} + Xm({1})*q3{0}{4} + Xp({1})*q3{0}{5} + (1-(T31 + T32 + wm({0}) + wp({0}) + Xm({1}) + Xp({1}))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q3{0}{1}".format(int(k),int(h)))


print("{", end='')
for v in var_list:
	print("{}, ".format(v), end='')

print("}")
	
