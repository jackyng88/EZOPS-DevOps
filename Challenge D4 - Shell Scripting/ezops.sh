#!/bin/bash

wget -O train.csv "https://www.kaggle.com/c/titanic/download/train.csv"

wget -O alphavantage.csv "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv"

awk  'BEGIN{
  FS=OFS=","                       # set the field delimiter
}
{                                  # execute only on non empty line
  for(i=NF;i>=1;i--)               # loop through all elements
    printf "%s", $i (i==1?ORS:OFS) # print the parameter together with the comma or newline 
}' train.csv > reverse.csv


awk 'BEGIN{FS=","} {s=$NF; for (i=1; i<=NF; i+=2) printf ("%s%c", $i, i + 2 <= NF ? "," : "\n") }' train.csv > every_other.csv

awk -F, 'function rev(x) {r=""; 
                            for(j=length(x);j;j--) r=r substr(x,j,1); 
                            return r}
           BEGIN {OFS=FS} 
                 {for(i=1;i<NF;i+=3) $i=rev($i)}1' train.csv > reverse_third_col.csv
