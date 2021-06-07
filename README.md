# symobological

Solver for symbolism puzzles as found in [IQ Puzzles](https://www.barnesandnoble.com/w/iq-puzzles-puzzlewright-press/1131511819)

## Puzzle input format

Takes an 5x5 grid of symbols as input, plus the row and column totals. See test.txt for an example encoding.

## Usage

```bash
$ python3 solver.py test.txt
● ● ● ● ● 
✚ ✚ ✚ ✚ ✚ 
⬟ ⬟ ⬟ ⬟ ⬟ 
■ ■ ■ ■ ■ 
★ ★ ★ ★ ★ 

circle: 1
cross: 2
pentagon: 3
square: 4
star: 5
$
```
