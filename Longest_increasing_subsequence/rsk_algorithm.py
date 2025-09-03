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
