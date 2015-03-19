#!/bin/bash

for i in "$@"
do
case $i in
    -d=*|--delay=*)
    DELAY="${i#*=}"
    shift
    ;;
    -s=*|--size=*)
    SIZE="${i#*=}"
    shift
    ;;
    -dir=*|--directory=*)
    DIRECTORY="${i#*=}"
    shift
    ;;
esac
done

if [ -z "$SIZE" ]; then 
  SIZE=256 
fi 

if [ -z "$DELAY" ]; then 
  DELAY=30
fi 

if [ -z "$DIRECTORY" ]; then 
  DIRECTORY="."
fi 

#echo "DIR="$DIRECTORY
#echo "DELAY="$DELAY
#echo "SIZE="$SIZE

#resize
for file in $(ls $DIRECTORY | grep -i .JPG ); 
do 
  echo "Processing file" $DIRECTORY/$file
  CAPTION=$file
  #DAY="Day_$BASE"
  BASE=${file%.*}

  convert $DIRECTORY/$file -resize $SIZEx$SIZE\> -fill white -undercolor black  -gravity South  -annotate +5+5 $CAPTION $DIRECTORY/$BASE.small.jpg
done

#animate
echo "Generating result.gif" 
convert -delay $DELAY -loop 0 $DIRECTORY/*.small.jpg $DIRECTORY/result.gif
rm -rf $DIRECTORY/*.small.*
