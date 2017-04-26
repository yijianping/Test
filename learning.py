# -*- coding: utf-8 -*-

import numpy as np
from scipy import spatial


def cosine_similarity(vec_1, vec_2):
    return 1 - spatial.distance.cosine(vec_1, vec_2)


if __name__ == '__main__':
    vector_a = np.array([2, 3, 4, 5])
    vector_b = np.array([1, 1.5, 2, 2.5])

    print(cosine_similarity(vector_a, vector_b))
