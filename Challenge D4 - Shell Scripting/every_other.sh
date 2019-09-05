#!/bin/bash

awk 'BEGIN{FS=","} {s=$NF; for (i=1; i<=NF; i+=2) printf ("%s%c", $i, i + 2 <= NF ? "," : "\n") }' train.csv > every_other.csv
