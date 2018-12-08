for file in *parsed; do
a=$(grep -v "#" $file | wc -l)
b=$(grep -v "#" $file | cut -f1 | sort | uniq | wc -l)
c=$(grep -v "#" $file | awk '$2=="yes" {print $1}' | sort | uniq | wc -l);
echo -e $file'\t'$a'\t'$b'\t'$c >> uTRuGuPCG.txt;
done
