set terminal pdfcairo size 9, 4.5
set output "comparison_C_k.pdf"


set xrange [0.9:105]
set yrange [1e-6:9e-1]
set key font "Helvetica, 43" 
set xlabel font "Helvetica,46" 
set xtics font "Helvetica,43"
set ylabel font "Helvetica,46" 
set ytics font "Helvetica,43"
set lmargin at screen 0.16
set bmargin at screen 0.16
set key left bottom

set label "(a)" at 50, 0.06 font "Helvetica, 60"

set log x
set log y
set xtics add ("10^{0}" 1e-0, "10^{1}" 1e1, "10^{2}" 1e2)
set mxtics 10

set xtics nomirror
set ytics nomirror

set ytics ("10^{-6}" 1e-6, "10^{-5}" 1e-5, "10^{-4}" 1e-4, "10^{-3}" 1e-3, "10^{-2}" 1e-2, "10^{-1}" 1e-1)
set xlabel "k"
set ylabel "C(k)"

set style data points
plot "./N100_C_k.dat" u 1:2:3 w yerrorbars lc rgb "black" pt 7 ps 0.8 t "", \
		 './N100_C_k.dat' u 1:2 w lp ls 1 lc rgb "black" t "cABM", \
		 "./zeroR_nonzeroQ_C_k.dat" u 1:2:3 w yerrorbars lc rgb "orange" pt 7 ps 0.8 t "", \
		 './zeroR_nonzeroQ_C_k.dat' u 1:2 w lp ls 2 lc rgb "orange" t "R(m,n)=0", \
