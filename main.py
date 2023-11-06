def local_matrix(x_loc, y_loc, E, nu, rhof, n_ind, q, d_ind):
    # здесь вся работа по локальной генерации
    d1 = E / (2 * (1 - nu ** 2))
    d2 = E / (4 * (1 + nu))
    d3 = E * nu / (2 * (1 - nu ** 2))
