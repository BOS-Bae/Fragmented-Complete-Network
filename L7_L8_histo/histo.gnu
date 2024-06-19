set boxwidth 0.2 absolute
set style fill solid 0.2 
set title font "Helvetica,20"
set xtics font "Helvetica,15"
set ytics font "Helvetica,15"

set log y

set ytics 10
set xtics ("0,1,2|3|4" 0, "0|1,2|3|4" 1, "|0,4|1,2|3" 2, "0,1,2,4|3" 3, "Others" 4)
set yrange [1:1000]
set xrange [-0.5:4.5]

set title "L8, idx 2"
p "L8idx2_hist.dat" using ($1):(1) ls 2 t "" smooth frequency with boxes

pause mouse key
