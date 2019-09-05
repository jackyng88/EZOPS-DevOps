#!/bin/bash

awk  'BEGIN{
  FS=OFS=","                       # set the field delimiter
}
{                                  # execute only on non empty line
  for(i=NF;i>=1;i--)               # loop through all elements
    printf "%s", $i (i==1?ORS:OFS) # print the parameter together with the comma or newline 
}' train.csv > reverse.csv

