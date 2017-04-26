# -*- coding: utf-8 -*-

import numpy as np
from scipy import spatial


def cosine_similarity(vec_1, vec_2):
    return 1 - spatial.distance.cosine(vec_1, vec_2)


if __name__ == '__main__':
    p_index = []
    for ele in open("C:/Users/Administrator/Desktop/index.txt").readlines():
        p_index.append(int(ele.strip('\n')))

    p_matrix = []
    for each_line in open("C:/Users/Administrator/Desktop/matrix.txt").readlines():
        each_line = each_line.strip('\n')
        elelist = each_line.split('\t')[0:288]
        elelist = [float(i) for i in elelist]
        elelist = np.asarray(elelist)
        p_matrix.append(elelist)

    print(cosine_similarity(p_matrix[0],p_matrix[1]))

