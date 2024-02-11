def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication
    """
    # Vérification si m_a et m_b sont des listes
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Vérification si m_a et m_b sont des listes de listes
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Vérification si m_a et m_b ne sont pas vides
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Vérification si les éléments de m_a et m_b sont des int ou float
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Vérification si toutes les lignes de m_a ont la même taille
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    # Vérification si toutes les lignes de m_b ont la même taille
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    # Vérification si m_a et m_b peuvent être multipliées
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Calcul de la multiplication de m_a et m_b
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
