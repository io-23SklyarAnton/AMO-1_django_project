from .algorithms import linear_algorithm, branches_algorithm, cyclic_algorithm
import os
import re


def algorithm_result_from_file(algorithm_func, file):
    try:
        data = (file.read()).decode()
        numbers = re.findall('\d+', data)
        return algorithm_func(*map(int, numbers))
    except Exception:
        return 'incorrect file format, send txt file with separated numbers like: 12 3 4 OR 1,2,3 OR a=1 b=2'
