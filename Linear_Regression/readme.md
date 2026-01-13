# Linear Regression
We have `y = kx + b` like func and somehow need to make this line as near as possible to every points.

### Simple Way
Just move `k` (angle) and `b` (y-intersection) a little to every points separately. For example:  
##### IN:
- line `p'' = mr + b` (p'' like "p with hat"), where `p` - price of house, `m` - price of one flat, `b` - base price (with 0 flats).
- point `(r, p)`
##### Algorithm:
- choose some random low-value `n1` and `n2` (greek letters like n-nose letter)
##### Scenario 1. Point in the *Ist quadrant*:
- `m' = m + n1` to turn the line counterclockwise
- `b' = b + n2` to move the line upper
##### Scenario 2. Point in the *IInd quadrant*:
- `m' = m - n1` to turn the line clockwise
- `b' = b + n2` to move the line upper
##### Scenario 3. Point in the *IIIrd quadrant*:
- `m' = m + n1` to turn the line counterclockwise
- `b' = b - n2` to move the line lower
##### Scenario 4. Point in the *IVth quadrant*:
- `m' = m - n1` to turn the line clockwise
- `b' = b - n2` to move the line lower
##### OUT:
- line `p'' = m'r + b'`

### Quadratic way  
1. If point is *above* the line, we **increase** a little to `b`. Otherwise - **decrease**.
2. If point is *above* the line, `p-p''` **> 0**. Otherwise - **< 0**.
So if we add `p-p''` to `b`, line will always move to point.  
3. In the *Simple Way* scenarios 1 or 3, we turn the line *counterclockwise*. Otherwise - *clockwise*.
4. If `(r, p)` on the right from vertical axis, **r > 0**. Otherwise - **r < 0**.
Consider that `r(p-p'')` **> 0**, when `r`, `p-p''` **BOTH > 0 or < 0**. This is what we want (*scenarios 1, 3*). Similarly `r(p-p'')` **< 0** in *scenarios 2, 4*.  
##### IN:
- the line with angle `m`, y-intersection `b` and equation `p'' = mr + b`
- point `(r, p)`
- a little `n` (speed of learning)
##### Algorithm:
- add `nr(p-p'')` to angle `m` equals `m' = m + nr(p-p'')` (the line is rotating)
- add `nr(p-p'')` to y-intersection `b` equals `b' = b + n(p-p'')` (it moves the line)
##### OUT:
- line `p'' = m'r + b'`
