from collections import deque

def action(state):
    loc, a, b = state
    actions = []
    if (loc == 'A' and a == 'brudny') or (loc == 'B' and b == 'brudny'):
        actions.append('ssij')
    if loc == 'A':
        actions.append('prawo')
    elif loc == 'B':
        actions.append('lewo')
    return actions

# RESULT(state, action) - stan po wykonaniu akcji
def result(state, act):
    loc, a, b = state
    if act == 'ssij':
        if loc == 'A':
            return (loc, 'czysty', b)
        else:
            return (loc, a, 'czysty')
    elif act == 'lewo':
        return ('A', a, b)
    elif act == 'prawo':
        return ('B', a, b)
    return state

# CEL - oba pola czyste
def is_goal(state):
    _, a, b = state
    return a == 'czysty' and b == 'czysty'

# BFS - Breadth First Search
def bfs(start_state):
    queue = deque()
    queue.append((start_state, []))  # (stan, ścieżka_akcji)
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        # Debug: co robi odkurzacz
        loc, a, b = state
        print(f"\n🧠 Aktualny stan: Odkurzacz w {loc}, A={a}, B={b}")
        print(f"🔁 Dotychczasowa ścieżka: {path}")

        if is_goal(state):
            print("\nCEL OSIĄGNIĘTY!")
            print("📝 Ścieżka działań:")
            for step in path:
                print(f" {step}")
            return

        for act in action(state):
            new_state = result(state, act)
            queue.append((new_state, path + [act]))

initial_state = ('A', 'brudny', 'brudny')

bfs(initial_state)


#1. {Loc(A), Dirty(A), Dirty(B)}
#2. {Loc(A), Clean(A), Dirty(B)}
#3. {Loc(A), Dirty(A), Clean(B)}
#4. {Loc(A), Clean(A), Clean(B)}
#5. {Loc(B), Dirty(A), Dirty(B)}
#6. {Loc(B), Clean(A), Dirty(B)}
#7. {Loc(B), Dirty(A), Clean(B)}
#8. {Loc(B), Clean(A), Clean(B)}