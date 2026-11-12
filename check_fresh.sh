#!/bin/sh
# Checks that the n = 20 files in data/ (fetched by fetch_data.sh from download/configurations/) agree line for line with
# the n = 20 part of Flammenkamp's current complete file download/all_known_solutions (the up-to-date database: on
# 13 Nov 2026 it was dated 2026-10-28 and its largest grid size was n = 78). Neither file is redistributed here.
set -e
mkdir -p data
curl -fsS -o data/all_known_solutions "https://wwwhomes.uni-bielefeld.de/achim/no3in/download/all_known_solutions"
echo "largest n in all_known_solutions: $(awk '{n=(length($0)-1)/2; if(n>m)m=n} END{print m}' data/all_known_solutions)"
awk 'length($0)==41' data/all_known_solutions | tr -d '\r' | sort > data/n20-all.txt
cat data/n20_iden data/n20_dia1 data/n20_dia2 data/n20_rot2 data/n20_rot4 | tr -d '\r' | grep -v '^$' | sort > data/n20-config.txt
wc -l < data/n20-all.txt
cmp data/n20-all.txt data/n20-config.txt && echo "the n = 20 lines agree"
