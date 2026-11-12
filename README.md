# Tiny Chess Engine

A chess engine in 4 KB of Python for the make.fun bounty
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

0x88 board, negamax with alpha-beta + quiescence, transposition table,
MVV-LVA + killer move ordering, piece-square eval, fixed node budget
(never a clock, so live and replay agree). Standard library only.
