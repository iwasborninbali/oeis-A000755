# OEIS A000755: no-three-in-line configurations on a square grid

[A000755](https://oeis.org/A000755) counts placements of 2n points in the n × n grid with no three collinear; rotations and reflections are counted separately. The contribution credited to Aleksei Kudriashov in the OEIS is **a(20) = 941580** (23 August 2026), obtained from Achim Flammenkamp's database and checked by orbit sums.

## Data and method

The check uses the five n=20 representative files from [Flammenkamp's configurations](https://wwwhomes.uni-bielefeld.de/achim/no3in/download/configurations/). They are not redistributed here; `./fetch_data.sh` downloads them into `data/` (our check of 8 November 2026 used the files as served that day). Each line encodes two points per row. `common.py` decodes the format and generates all eight square symmetries. `check_orbits.py` checks representative counts, orbit sizes and distinctness of the canonical orbits and sums their sizes:

| Class | Representatives | Orbit size | Placements |
|---|---:|---:|---:|
| iden | 117347 | 8 | 938776 |
| dia1 | 17 | 4 | 68 |
| dia2 | 2 | 2 | 4 |
| rot2 | 675 | 4 | 2700 |
| rot4 | 16 | 2 | 32 |
| Total | 118057 | | 941580 |

Run `./fetch_data.sh` and then `python3 -B check_orbits.py` from this directory. This checks the orbit arithmetic and duplicates, not completeness of the original enumeration. A separate earlier computation checked all expanded configurations for collinearity; it is not repeated by this short check. The full database is available from [the original download directory](https://wwwhomes.uni-bielefeld.de/achim/no3in/download/).

## History, credit and licence

The OEIS sequence is by N. J. A. Sloane; it credits further terms to Achim Flammenkamp, a(17) and a(18) to Benjamin Chaffin, and a(19) to Mitchell Riley. The database and its source enumeration are due to Achim Flammenkamp and contributors credited by him; our orbit sum does not independently prove completeness. The data files are third-party material and remain subject to their source terms; no new licence is asserted over them. For original repository code and text: MIT and CC BY 4.0 respectively, see [LICENSE.md](LICENSE.md). Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance.
