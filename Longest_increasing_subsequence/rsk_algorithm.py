def rsk_insert(tableau, x):
    """
    Inserts x into a Young tableau. Modifies the tableau in place.
    """
    for i in range(len(tableau)):
        row = tableau[i]
        try:
            j = next(j for j, y in enumerate(row) if y > x)
            row[j], x = x, row[j]  # swap
            return
        except StopIteration:
            row.append(x)
            return
    tableau.append([x])

def rsk_build_tableau(p):
    tableau = []
    for x in p:
        rsk_insert(tableau, x)
    return tableau

def rsk_insert_animated(tableau, x):
    """
    Performs one step of RSK insertion on a copy of the tableau.
    Returns the new tableau and the bumping path.
    A bumping path is a list of tuples: (row, col, old_val, new_val)
    """
    new_tableau = [list(row) for row in tableau]
    path = []

    for i in range(len(new_tableau)):
        row = new_tableau[i]
        try:
            j = next(j for j, y in enumerate(row) if y > x)
            old_val = row[j]
            row[j] = x
            path.append((i, j, old_val, x))
            x = old_val
        except StopIteration:
            row.append(x)
            path.append((i, len(row) - 1, None, x))  # Appended
            return new_tableau, path

    new_tableau.append([x])
    path.append((len(new_tableau) - 1, 0, None, x))  # Appended to new row
    return new_tableau, path