edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 5).
edge(c, e, 3).
edge(c, f, 4).
edge(d, g, 7).
edge(e, g, 6).
edge(f, g, 8).
search(Node, Node, [Node], 0).
search(Start, Goal, Path, Cost) :-
    best_first(Start, Goal, Path, [], Cost).
best_first(Node, Node, [Node], Visited, 0).
best_first(Start, Goal, [Start | Path], Visited, TotalCost) :-
    connected(Start, Next, Cost),
    not(member(Next, Visited)),
    best_first(Next, Goal, Path, [Start | Visited], RemainingCost),
    TotalCost is RemainingCost + Cost.
connected(From, To, Cost) :- edge(From, To, Cost).
connected(From, To, Cost) :- edge(To, From, Cost).
