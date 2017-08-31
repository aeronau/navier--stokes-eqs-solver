import numpy as np

def halo_update(F, N):

    F[1, :] = F[N + 1, :]
    F[N + 2, :] = F[2, :]

    F[:, 1] = F[:, N + 1]
    F[:, N + 2] = F[:, 2]
