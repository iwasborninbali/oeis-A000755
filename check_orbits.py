from collections import Counter
from pathlib import Path
from common import decode, orbit

expected = {'n20_iden': (117347, 8), 'n20_dia1': (17, 4), 'n20_dia2': (2, 2), 'n20_rot2': (675, 4), 'n20_rot4': (16, 2)}
seen = set()
total = 0
for name, (count, size) in expected.items():
    rows = 0
    for line in (Path(__file__).parent / 'data' / name).read_text().splitlines():
        n, xs = decode(line)
        assert n == 20
        group = orbit(xs)
        assert len(group) == size, (name, rows, len(group))
        canonical = group[0]
        assert canonical not in seen, (name, rows)
        seen.add(canonical)
        total += len(group)
        rows += 1
    assert rows == count, (name, rows)
    print(f'{name}: {rows} representatives, orbit size {size}, placements {rows * size}', flush=True)
assert len(seen) == 118057 and total == 941580
print(f'{len(seen)} distinct orbits; {total} placements')
