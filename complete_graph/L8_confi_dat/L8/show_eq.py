import sys

if (len(sys.argv) < 2):
	print("python3 show_eq.py m n") 
	print("[!] In this code, m and n should be larger than 1,") 
	print("because the case like 'n-1 == 0' is not included due to the convenience.") 
	exit(1)

m = int(sys.argv[1])
n = int(sys.argv[2])
N = m+n

print("NSolve[")
var_list = []
# for state 1
for k in range(0, n):
	for h in range(0,m):
		if (k==0 and h!=0 and h!=m-1 and n-1 != 0):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Op[{0},{1}]*q1l{2}l{1} + Zm[{1}]*q1l{0}l{3} + Zp[{0},{1}]*q1l{0}l{4} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (n-1 != 0 and k==n-1 and h!=0 and h!=m-1):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*qp[{3}] + Zm[{1}]*q1l{0}l{4} + Zp[{0},{1}]*q1l{0}l{5} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0 and n-1 != 0):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Op[{0},{1}]*q1l{2}l{1} + Zp[{0},{1}]*q1l{0}l{3} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (n-1 != 0 and k==n-1 and h==0):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*qp[{3}]+ Zp[{0},{1}]*q1l{0}l{4} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Om[{0}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-1 and n-1 != 0):
			print("q1l{0}l{1} == T13[{0}]*rp[{2}] + Op[{0},{1}]*q1l{2}l{1} + T12[m-1]*rn[{2}] + Zm[{1}]*q1l{0}l{3} + (1-(T13[{0}] + Op[{0},{1}] + Zm[{1}] + T12[m-1]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1)))
		elif (k==n-1 and h==m-1 and n-1 != 0):
			print("q1l{0}l{1} == Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*qp[{3}] + T12[m-1]*rn[{5}] + T13[{0}]*rp[{5}] + Zm[{1}]*q1l{0}l{4} + (1-(Om[{0}] + Op[{0},{1}] + Zm[{1}] + T12[m-1] + T13[{0}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n-1):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*q1l{3}l{1} + Zp[{0},{1}]*q1l{0}l{4} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))
		elif (h==m-1 and k!=0 and k!=n-1):
			print("q1l{0}l{1} == Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*q1l{3}l{1} + T12[m-1]*rn[{3}] + T13[{0}]*rp[{3}] + Zm[{1}]*q1l{0}l{4} + (1-(Om[{0}] + Op[{0},{1}] + Zm[{1}] + T12[m-1] + T13[{0}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))

		elif (k==n-1 and n-1 == 0 and h!=0 and h!=m-1):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Op[{0},{1}]*qp[{4}] + Zm[{1}]*q1l{0}l{3} + Zp[{0},{1}]*q1l{0}l{4} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n-1 and n-1 == 0 and h==0):
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Op[{0},{1}]*qp[{3}] + Zp[{0},{1}]*q1l{0}l{3} + (1-(T12[{1}] + T13[{0}] + Op[{0},{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n-1 and n-1 == 0 and h==m-1):
			print("q1l{0}l{1} == T13[{0}]*rp[{2}] + Op[{0},{1}]*qp[{4}] + T12[m-1]*rn[{2}] + Zm[{1}]*q1l{0}l{3} + (1-(T13[{0}] + Op[{0},{1}] + Zm[{1}] + T12[m-1]))*q1l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(h+1)))
		else: 			
			print("q1l{0}l{1} == T12[{1}]*q2l{0}l{1} + T13[{0}]*q3l{0}l{1} + Om[{0}]*q1l{2}l{1} + Op[{0},{1}]*q1l{3}l{1} + Zm[{1}]*q1l{0}l{4} + Zp[{0},{1}]*q1l{0}l{5} + (1-(T12[{1}] + T13[{0}] + Om[{0}] + Op[{0},{1}] + Zm[{1}] + Zp[{0},{1}]))*q1l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q1l{0}l{1}".format(int(k),int(h)))


# for state 2
for k in range(0, n):
	for h in range(0,m-1):
		if (k==0 and h!=0 and h!=m-2 and n-1 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*q2l{2}l{1} + Xm[{1}]*q2l{0}l{3} + Xp[{0},{1}]*q2l{0}l{4} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n-1 and h!=0 and h!=m-2 and n-1 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*qn[{3}] + Xm[{1}]*q2l{0}l{4} + Xp[{0},{1}]*q2l{0}l{5} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0 and m-2 != 0 and n-1 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*q2l{2}l{1} + Xp[{0},{1}]*q2l{0}l{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n-1 and h==0 and n-1 != 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*qn[{3}]+ Xp[{0},{1}]*q2l{0}l{4} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Om[{0}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-2 and n-1 != 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*q2l{2}l{1} + Xp[{0},{1}]*rn[{4}] + Xm[{1}]*q2l{0}l{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1)))
		elif (k==n-1 and h==m-2 and n-1 != 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*qn[{3}] + Xp[{0},{1}]*rn[{5}] + Xm[{1}]*q2l{0}l{4} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n-1 and n-1 != 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*q2l{3}l{1} + Xp[{0},{1}]*q2l{0}l{4} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))

		elif (h==m-2 and k!=0 and k!=n-1 and n-1 != 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*q2l{3}l{1} + Xm[{1}]*q2l{0}l{4} + Xp[{0},{1}]*rn[{3}] + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))
		
		elif (h==m-2 and m-2 == 0 and k!= 0 and k!= n-1 and n-1 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*q2l{3}l{1} + Xp[{0},{1}]*rn[{3}] + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))
		elif (h==m-2 and m-2 == 0 and n-1 != 0 and k == 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*q2l{2}l{1} + Xp[{0},{1}]*rn[{2}] + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (h==m-2 and m-2 == 0 and n-1 != 0 and k == n-1):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*qn[{3}]+ Xp[{0},{1}]*rn[{5}] + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Om[{0}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1), int(k+1)))
		elif (h==m-2 and m-2 == 0 and k==n-1 and  n-1 == 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*qn[{3}] + Xp[{0},{1}]*rn[{2}] + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
	
		elif (k==n-1 and n-1 == 0 and h!= m-2 and h!= 0 and m-2 != 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*qn[{4}] + Xp[{0},{1}]*q2l{0}l{4} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))
			
		elif (k==n-1 and n-1 == 0 and m-2 != 0 and h == 0):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*qn[{3}] + Xp[{0},{1}]*q2l{0}l{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
			
		elif (k==n-1 and n-1 == 0 and m-2 != 0 and h == m-2):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*qn[{5}] + Xp[{0},{1}]*rn[{4}] + Xm[{1}]*q2l{0}l{3} + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1), int(h+1)))
			
		elif (k==n-1 and n-1 == 0 and m-2 == 0 and h == m-2):
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Op[{0},{1}]*qn[{3}] + Xp[{0},{1}]*rn[{2}] + (1-(T21[{1}] + T23[{0}] + Op[{0},{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		else: 			
			print("q2l{0}l{1} == T21[{1}]*q1l{0}l{1} + T23[{0}]*q3l{0}l{1} + Om[{0}]*q2l{2}l{1} + Op[{0},{1}]*q2l{3}l{1} + Xm[{1}]*q2l{0}l{4} + Xp[{0},{1}]*q2l{0}l{5} + (1-(T21[{1}] + T23[{0}] + Om[{0}] + Op[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q2l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q2l{0}l{1}".format(int(k),int(h)))


# for state 3
for k in range(0, n+1):
	for h in range(0,m-1):
		if (k==0 and h!=0 and h!=m-2):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wp[{0},{1}]*q3l{2}l{1} + Xm[{1}]*q3l{0}l{3} + Xp[{0},{1}]*q3l{0}l{4} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1),int(h+1)))
		elif (k==n and h!=0 and h!=m-2):
			print("q3l{0}l{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3l{2}l{1} + T32[n]*qn[{3}] + Xm[{1}]*q3l{0}l{4} + Xp[{0},{1}]*q3l{0}l{5} + (1-(wm[{0}] + T31[{1}] + T32[n] + Xm[{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h-1),int(h+1)))
		elif (k==0 and h==0 and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wp[{0},{1}]*q3l{2}l{1} + Xp[{0},{1}]*q3l{0}l{3} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (k==n and h==0 and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3l{2}l{1} + T32[n]*qn[{3}] + Xp[{0},{1}]*q3l{0}l{4} + (1-(T31[{1}] + T32[n] + wm[{0}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(h+1),int(h+1)))
		elif (k==0 and h==m-2 and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wp[{0},{1}]*q3l{2}l{1} + Xp[{0},{1}]*rp[{4}] + Xm[{1}]*q3l{0}l{3} + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h-1), int(k+1)))

		elif (k==n and h==m-2 and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*qp[{3}] + T32[n]*qn[{3}] + wm[{0}]*q3l{2}l{1} + Xp[{0},{1}]*rp[{5}] + Xm[{1}]*q3l{0}l{4} + (1-(T31[{1}] + T32[n] + wm[{0}] + Xm[{1}] + Xp[{0},{1}]))*q3l{0}l{1},".format(int(k),int(h),int(k-1),int(h+1),int(h-1), int(k+1)))
		elif (h==0 and k!=0 and k!=n and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wm[{0}]*q3l{2}l{1} + wp[{0},{1}]*q3l{3}l{1} + Xp[{0},{1}]*q3l{0}l{4} + (1-(T31[{1}] + T32[{0}] + wm[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))
		elif (h==m-2 and k!=0 and k!=n and m-2 != 0):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wm[{0}]*q3l{2}l{1} + wp[{0},{1}]*q3l{3}l{1} + Xm[{1}]*q3l{0}l{4} + Xp[{0},{1}]*rp[{3}]+ (1-(T32[{0}] +T31[{1}] + wm[{0}] + wp[{0},{1}] + Xp[{0},{1}] + Xm[{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1)))

		elif (h==m-2 and m-2 == 0 and k!=0 and k!=n):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wm[{0}]*q3l{2}l{1} + wp[{0},{1}]*q3l{3}l{1} + Xp[{0},{1}]*rp[{3}] + (1-(T31[{1}] + T32[{0}] + wm[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h+1)))
		elif (h==m-2 and m-2 == 0 and k==0):
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wp[{0},{1}]*q3l{2}l{1} + Xp[{0},{1}]*rp[{2}] + (1-(T31[{1}] + T32[{0}] + wp[{0},{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k+1),int(h+1)))
		elif (h==m-2 and m-2 == 0 and k==n):
			print("q3l{0}l{1} == T31[{1}]*qp[{3}] + wm[{0}]*q3l{2}l{1} + T32[n]*qn[{3}] + Xp[{0},{1}]*rp[{5}] + (1-(T31[{1}] + T32[n] + wm[{0}] + Xp[{0},{1}]))*q3l{0}l{1}, ".format(int(k),int(h),int(k-1),int(h+1),int(h+1), int(k+1)))
	

	
		else: 			
			print("q3l{0}l{1} == T31[{1}]*q1l{0}l{1} + T32[{0}]*q2l{0}l{1} + wm[{0}]*q3l{2}l{1} + wp[{0},{1}]*q3l{3}l{1} + Xm[{1}]*q3l{0}l{4} + Xp[{0},{1}]*q3l{0}l{5} + (1-(T31[{1}] + T32[{0}] + wm[{0}] + wp[{0},{1}] + Xm[{1}] + Xp[{0},{1}]))*q3l{0}l{1} &&".format(int(k),int(h),int(k-1),int(k+1),int(h-1),int(h+1)))
		var_list.append("q3l{0}l{1}".format(int(k),int(h)))

print("{", end='')
for v in var_list:
	if (v != var_list[-1]):
		print("{}, ".format(v), end='')
	else:
		print("{} ".format(v), end='')
print("}]")
