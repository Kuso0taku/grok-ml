# Linear Regression
We have `y = kx + b` like func and somehow need to make this line as near as possible to every dots.

### Simple Way
Just move `k` (angle) and `b` (y-intersection) a little to every dots separately. For example:  
***IN:**  
- line `p'' = mr + b` (p'' like "p with hat"), 
- dot (r, p)
**Algorithm:**
- choose some random low-value `n1` and `n2` (greek letters like n-nose letter)
**Scenario 1** dot in the *Ist quadrant*:
- `m' = m + n1` to turn the line counterclockwise
- `b' = b + n2` to move the line upper
**Scenario 2** dot in the *IInd quadrant*:
- `m' = m - n1` to turn the line clockwise
- `b' = b + n2` to move the line upper
**Scenario 3** dot in the *IIIrd quadrant*:
- `m' = m + n1` to turn the line counterclockwise
- `b' = b - n2` to move the line lower
**Scenario 4** dot in the *IVth quadrant*:
- `m' = m - n1` to turn the line clockwise
- `b' = b - n2` to move the line lower
