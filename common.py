"""Independent Python decoding and D4 operations (zero based x,y)."""
from collections import Counter
from math import gcd

ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,.'
CLASSES = dict(zip('.:/-ocx+*', ['iden','rot2','dia1','ort1','rot4','rct4','dia2','ort2','full']))

def decode(line):
    line = line.strip()
    assert line[0] in CLASSES and (len(line)-1)%2 == 0
    n = (len(line)-1)//2
    xs = tuple(ALPHABET.index(c) for c in line[1:])
    assert all(0 <= x < n for x in xs)
    assert all(xs[2*y] < xs[2*y+1] for y in range(n))
    assert Counter(xs) == Counter({x:2 for x in range(n)})
    return n, xs

def points(xs):
    return tuple((x,k//2) for k,x in enumerate(xs))

def rowcode(pts):
    return tuple(x for x,y in sorted(pts,key=lambda p:(p[1],p[0])))

def transforms(xs):
    n = len(xs)//2
    p = points(xs)
    out = []
    for mirror in range(2):
        q = tuple((n-1-x,y) if mirror else (x,y) for x,y in p)
        for rotation in range(4):
            out.append(rowcode(q))
            q = tuple((n-1-y,x) for x,y in q)
    return tuple(out)

def orbit(xs):
    return sorted(set(transforms(xs)))

def canonical(xs):
    return min(transforms(xs))

def exact_check(xs):
    """No repeated primitive direction from any anchor: exact integer arithmetic."""
    n = len(xs)//2
    assert len(xs) == 2*n
    p = points(xs)
    assert len(set(p)) == len(p)
    assert all(0<=x<n and 0<=y<n for x,y in p)
    assert Counter(x for x,y in p)==Counter({x:2 for x in range(n)})
    for i,(x,y) in enumerate(p):
        seen = set()
        for u,v in p[i+1:]:
            dx,dy=u-x,v-y
            g=gcd(abs(dx),abs(dy)); dx//=g; dy//=g
            if dx<0 or (dx==0 and dy<0): dx=-dx; dy=-dy
            assert (dx,dy) not in seen, ('collinear',i,(dx,dy))
            seen.add((dx,dy))
    return True

def symmetry(xs):
    ts=transforms(xs)
    fixed=[k for k,t in enumerate(ts) if t==xs]
    if len(fixed)==8: return 'full'
    if 1 in fixed: return 'rot4'
    # In this transformation convention 4,6 are orthogonal mirrors, 5,7 diagonal.
    orth=sum(k in fixed for k in (4,6))
    diag=sum(k in fixed for k in (5,7))
    if orth==2: return 'ort2'
    if diag==2: return 'dia2'
    if orth: return 'ort1'
    if diag: return 'dia1'
    if 2 in fixed: return 'rot2'
    assert len(fixed)==1
    return 'iden'
