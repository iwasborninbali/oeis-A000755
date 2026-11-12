#!/bin/sh
# Download the n = 20 representative files from Achim Flammenkamp's no-three-in-line database into data/.
# They are not redistributed here; all rights in them belong to their author.
set -e
mkdir -p data
for f in n20_iden n20_dia1 n20_dia2 n20_rot2 n20_rot4; do
  curl -fsS -o "data/$f" "https://wwwhomes.uni-bielefeld.de/achim/no3in/download/configurations/$f"
done
echo "downloaded into data/"
