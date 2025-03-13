set terminal pdfcairo size 9, 4.5
set output "Fig2b.pdf"


set xrange [0.9:500]
set yrange [0.005:1.5]
set key font "Helvetica, 45" 
set xlabel font "Helvetica,46" 
set xtics font "Helvetica,43"
set ylabel font "Helvetica,46" 
set ytics font "Helvetica,43"
set lmargin at screen 0.16
set bmargin at screen 0.16
set key left bottom

set label "(b)" at 200, 0.65 font "Helvetica, 60"
set log x
set log y

set xtics add ("10^{0}" 1e-0, "10^{1}" 1e1, "10^{2}" 1e2)
set ytics ("10^{-3}" 1e-3, "10^{-2}" 1e-2, "10^{-1}" 1e-1, "10^{0}" 1e-0)


set mxtics 10

set xtics nomirror
set ytics nomirror

set xlabel "k"
set ylabel "C(k)"

set style data points
plot "./Germany.dat" u ($0+1):1 w lp lc rgb "purple" pt 7 ps 0.8 t "Germany", \
     "./UK.dat" u ($0+1):1 w lp lc rgb "blue" pt 9 ps 0.8 t "UK", \
     "./Spain.dat" u ($0+1):1 w lp lc rgb "green" pt 5 ps 0.8 t "Spain"
