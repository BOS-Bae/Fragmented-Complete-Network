set terminal pdfcairo size 9, 4.5
set output "p_frac.pdf"

set key font "Helvetica, 40" 
set xlabel font "Helvetica,46" 
set xtics font "Helvetica,40"
set ylabel font "Helvetica,46" 
set ytics font "Helvetica,40"

#set key left top
set key at 45, 0.9

set log x
set log y
set ytics add ("0.4" 0.4, "1" 1)
set xrange [5:50]
set yrange [0.35:1.1]
set xlabel "N"
set ylabel "f"

fileL7 = "L7_p_frac.dat"
fileL4 = "L4_p_frac.dat"

set style data points

p fileL7 u 1:2 w lp pt 7 ps 0.8 lc rgb "black" t "L7", \
  fileL4 u 1:2 w lp pt 7 ps 0.8 dt 2 lc rgb "black" t "L4"
