import sys

if (len(sys.argv) < 2):
	print("python3 show_eq.py m n") 
	exit(1)

m = int(sys.argv[1])
n = int(sys.argv[2])
N = m+n

var_list = []
# for state 1
for k in range(0, n):
	for h in range(0,m):
		if (k==0 and h!=0 and h!=m-1):
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Op[{0},{1}]*q1{2}{1} + Zm[{1}]*q1{0}{3} + Zp[{0},{1}]*q1{0}{4} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n-1 and h!=0 and h!=m-1):
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Om[{0}]*q1{2}{1} + Op[{0},{1}]*qp[{3}] + Zm[{1}]*q1{0}{4} + Zp[{0},{1}]*q1{0}{5} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0):
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Op[{0},{1}]*q1{2}{1} + Zp[{0},{1}]*q1{0}{3} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n-1 and h==0):
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Om[{0}]*q1{2}{1} + Op[{0},{1}]*qp[{3}]+ Zp[{0},{1}]*q1{0}{4} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Om[{0}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-1):
			print("q1{0}{1} == T13[{0}]*rp[{2}] + Op[{0},{1}]*q1{2}{1} + g1*qn[{4}] + Zm[{1}]*q1{0}{3} + (1-(T13[{0}] + Op[{0},{1}] + Zm[{1}] + g1))*q1{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1)))
		elif (k==n-1 and h==m-1):
			print("q1{0}{1} == T13[{0}]*rp[{3}] + Om[{0}]*q1{2}{1} + Op[{0},{1}]*qp[{3}] + g1*qn[{5}] + Zm[{1}]*q1{0}{4} + (1-(T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}] + g1))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n-1):
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Om[{0}]*q1{2}{1} + Op[{0},{1}]*q1{3}{1} + Zp[{0},{1}]*q1{0}{4} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))

		elif (h==m-1 and k!=0 and k!=n-1):
			print("q1{0}{1} == T13[{0}]*rp[{3}] + Om[{0}]*q1{2}{1} + Op[{0},{1}]*q1{3}{1} + g1*qn[{3}] + Zm[{1}]*q1{0}{4} + (1-(T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}]) + g1)*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))
		else: 			
			print("q1{0}{1} == T12[{1}]*q2{0}{1} + T13[{0}]*q3{0}{1} + Om[{0}]*q1{2}{1} + Op[{0},{1}]*q1{3}{1} + Zm[{1}]*q1{0}{4} + Zp[{0},{1}]*q1{0}{5} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q1{0}{1}".format(int(k),int(h)))


# for state 2
for k in range(0, n):
	for h in range(0,m-1):
		if (k==0 and h!=0 and h!=m-2):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Op[{0},{1}]*q2{2}{1} + Xm[{1}]*q2{0}{3} + Xp[{0},{1}]*q2{0}{4} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n-1 and h!=0 and h!=m-2):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*qn[{3}] + Xm[{1}]*q2{0}{4} + Xp[{0},{1}]*q2{0}{5} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Op[{0},{1}]*q2{2}{1} + Xp[{0},{1}]*q2{0}{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n-1 and h==0):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*qn[{3}]+ Xp[{0},{1}]*q2{0}{4} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Om[{0}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-2):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Op[{0},{1}]*q2{2}{1} + Xp[{0},{1}]*rn[{4}] + Xm[{1}]*q2{0}{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1)))
		elif (k==n-1 and h==m-2):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*qn[{3}] + Xp[{0},{1}]*rn[{5}] + Xm[{1}]*q2{0}{4} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n-1):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*q2{3}{1} + Xp[{0},{1}]*q2{0}{4} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))

		elif (h==m-2 and k!=0 and k!=n-1):
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T13[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*q2{3}{1} + Xm[{1}]*q2{0}{4} + Xp[{0},{1}]*rn[{3}] + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))
		else: 			
			print("q2{0}{1} == T21[{1}]*q1{0}{1} + T23[{0}]*q3{0}{1} + Om[{0}]*q2{2}{1} + Op[{0},{1}]*q2{3}{1} + Xm[{1}]*q2{0}{4} + Xp[{0},{1}]*q2{0}{5} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q2{0}{1}".format(int(k),int(h)))


# for state 3
for k in range(0, n+1):
	for h in range(0,m-1):
		if (k==0 and h!=0 and h!=m-2):
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wp[{0},{1}]*q3{2}{1} + Xm[{1}]*q3{0}{3} + Xp[{0},{1}]*q3{0}{4} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n and h!=0 and h!=m-2):
			print("q3{0}{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3{2}{1} + g3*qn[{3}] + Xm[{1}]*q3{0}{4} + Xp[{0},{1}]*q3{0}{5} + (1-(T31[{1}] + wm[{0}] + g3 + Xm[{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0):
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wp[{0},{1}]*q3{2}{1} + Xp[{0},{1}]*q3{0}{3} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n and h==0):
			print("q3{0}{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3{2}{1} + g3*qn[{3}]+ Xp[{0},{1}]*q3{0}{4} + (1-(T31[{1}] + g3 + wm[{0}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-2):
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wp[{0},{1}]*qn[{4}] + Xp[{0},{1}]*rp[{4}] + Xm[{1}]*q3{0}{3} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1)))

		elif (k==n and h==m-2):
			print("q3{0}{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3{2}{1} + wp[{0},{1}]*qn[{3}] + Xp[{0},{1}]*rp[{5}] + Xm[{1}]*q3{0}{4} + (1-(T31[{1}] + wm[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3{0}{1},".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n):
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wm[{0}]*q3{2}{1} + wp[{0},{1}]*q3{3}{1} + Xp[{0},{1}]*q3{0}{4} + (1-(T31[{1}] + T32[{0}] + wm[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))

		elif (h==m-2 and k!=0 and k!=n):
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wm[{0}]*q3{2}{1} + wp[{0},{1}]*q3{3}{1} + Xm[{1}]*q3{0}{4} + Xp[{0},{1}]*rp[{3}]+ (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xp[{0},{1}] + Xm[{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))
		else: 			
			print("q3{0}{1} == T31[{1}]*q1{0}{1} + T32[{0}]*q2{0}{1} + wm[{0}]*q3{2}{1} + wp[{0},{1}]*q3{3}{1} + Xm[{1}]*q3{0}{4} + Xp[{0},{1}]*q3{0}{5} + (1-(T31[{1}] + T32[{0}] + wm[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3{0}{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q3{0}{1}".format(int(k),int(h)))

'''
for h in range(0,m-1):
	#var_list.append("q10{}".format(h))
	var_list.append("q1{}{}".format(n-1,h))
	#var_list.append("q20{}".format(h))
	var_list.append("q2{}{}".format(n-1,h))
	#var_list.append("q30{}".format(h))
	var_list.append("q3{}{}".format(n,h))

for k in range(0,n):
	#var_list.append("q1{}0".format(k))
	var_list.append("q1{}{}".format(k,m-1))
	#var_list.append("q2{}0".format(k))
	var_list.append("q2{}{}".format(k,m-2))
	#var_list.append("q3{}0".format(k))
	var_list.append("q3{}{}".format(k,m-2))
'''

print("{", end='')
for v in var_list:
	if (v != var_list[-1]):
		print("{}, ".format(v), end='')
	else:
		print("{} ".format(v), end='')
print("}")
	
