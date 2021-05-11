#!/bin/bash

n=0
inp=$1
while ! $inp && [ $n -le 5 ]; do
  sleep $n
  ((n=n+1))
  echo 'Retry' $n
done;
