#!/usr/bin/env bash

sed 's/JOURNALTITLE/JOURNAL/g' ./Ref_biber.bib > References1.bib
sed 's/DATE/YEAR/g' ./References1.bib > References.bib
bibtex2html -s abbrv -a -nofooter -noheader -nokeywords -noabstract References.bib 
rm References.bib
rm References1.bib
cp ./References_bib.html ..
