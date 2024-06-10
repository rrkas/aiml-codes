import pandas as pd
import numpy as np


def __del_cost(s: str):
    return len(s)


def __ins_cost(t: str):
    return len(t)


def __sub_cost(s: str, t: str):
    return (2 * len(s)) if s != t else 0


def min_edit_distance(
    source: str,
    target: str,
    del_cost_fn=__del_cost,
    ins_cost_fn=__ins_cost,
    sub_cost_fn=__sub_cost,
    debug=False,
) -> int:
    n = len(source)
    m = len(target)
    D = np.zeros((n + 1, m + 1))

    D[0, 0] = 0

    for i in range(1, n + 1):
        D[i, 0] = D[i - 1, 0] + del_cost_fn(source[i - 1])

    for j in range(1, m + 1):
        D[0, j] = D[0, j - 1] + ins_cost_fn(target[j - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i, j] = min(
                D[i - 1, j] + del_cost_fn(source[i - 1]),
                D[i - 1, j - 1] + sub_cost_fn(source[i - 1], target[j - 1]),
                D[i, j - 1] + ins_cost_fn(target[j - 1]),
            )

    if debug:
        e00 = "Src/Tar"
        D_oth = np.array(
            [(" " * len(e00)) for i in range((n + 2) * (m + 2))],
        ).reshape((n + 2, m + 2))
        D_oth[0, 0] = e00
        D_oth[0, 1:] = list("#" + target)
        D_oth[1:, 0] = list("#" + source)
        t = np.array([str(x) for x in D.flatten()]).reshape(D.shape)
        D_oth[1:, 1:] = t
        print(pd.DataFrame(D_oth).to_string(index=0, header=0))

    return D[n, n]


if __name__ == "__main__":
    import sys

    source, target = sys.argv[1], sys.argv[2]

    print(min_edit_distance(source, target, debug=True))
