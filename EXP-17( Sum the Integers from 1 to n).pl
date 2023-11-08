predicates
    add_upto(integer, integer)

clauses
   add_upto(1, 1)
   add_upto(N, Result) if
               N>=2,
               N_1=N-1,
               add_upto(N_1, Res),
               Result=Res+N.
goal
    add_upto(3, Result)
        Result=6
