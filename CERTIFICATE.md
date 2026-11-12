# Verification certificate

## Claim

- a(20) = 941580, obtained from the Flammenkamp database by orbit sums.
- Link to this repository for the orbit-sum check (queued).

## Evidence

| What | Repository path | Author and date | Coverage | Result | Independence / shared code or data |
|---|---|---|---|---|---|
| Third-party producer | Flammenkamp's configuration database, fetched using `fetch_data.sh` | Achim Flammenkamp and contributors credited by him; date of original enumeration not specified here | n=20 representatives in five symmetry classes | Database supplies 118057 representatives | Original data, not produced here |
| Orbit check | `check_orbits.py`, `common.py`, `fetch_data.sh` | Athanor lab, AI assisted; README reports check on 8 Nov 2026; individual coder not identified | Distinct representative orbits, sizes and total | 118057 orbits, 941580 placements on replay | Independent orbit arithmetic over the same third-party data; no independent generation, completeness proof or independent code comparison |
| Earlier validity check | README, Data and method | Author and date not specified | Expanded configurations' collinearity | Report only; code and log not identified | Unknown |

## Replayed for this repository

Executed on 13 Nov 2026 WITA, locally. Commands use the logged working directory; logs contain the full outputs. Wall times include process startup.

- `python3 -B check_orbits.py` — exit 0, 14.310 s; output: 118057 distinct orbits; 941580 placements. [`logs/certificate-2026-11-13/orbits.log`](logs/certificate-2026-11-13/orbits.log) (SHA-256 `3fa8fa9c419e251268b48c148b7bc5f53514a28892babd6216e68fd44f94ae58`).

The repository scripts were copied unchanged to `/tmp/c7-A000755`; the five data files were fetched there from the URLs in `fetch_data.sh` on 13 Nov 2026 WITA, each below 5 MB. Input SHA-256: `n20_dia1` `d330ec0e7b8defdce4284e7dbd3d9465cef5928650fbf71021f5796719262c7e`; `n20_dia2` `396fb5e8b9a9f0a2faba001390f6af9073d323a8ef63ec4a8cb3183c5d28ddfb`; `n20_iden` `13a390758d900264cb5b6ed83f6b703e5f14008b5f2ae4fdbb98df8c798be87d`; `n20_rot2` `d992247ae5be65bd5d35a344270bf8ff5418cc754b7c3a0964d41b337d1a8c0b`; `n20_rot4` `353b57d9f85c0ed9f9b6f996c3470463aad869c0b5f3dfcacab7d4716491c754`. Full independent enumeration was not replayed: no independent generator or runtime is supplied in this repository.

## Not covered

The database enumeration is not independently reproduced or proved complete. The orbit check does not test collinearity; the README describes an earlier check without a locally identified program or receipt. Thus the exact term depends on the source enumeration and that earlier reported validity check. The five inputs were downloaded anew; no historical checksums were provided to compare with the 8 Nov data. Link availability was not checked.

## Guide's independent check

pending

## Verdict

partial — The evidence and replay leave the gaps above, and the Guide's independent check is pending.
