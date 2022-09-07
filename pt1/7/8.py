from matplotlib import pyplot as plt
import seaborn as sns


def cm(inch):
    return inch/2.4


def nthmax(arr2d, n=2):
    assert n>=2
    arr2d_sort = sorted([v for li in arr2d for v in li], reverse=True)
    return arr2d_sort[n-1]


def nthmin(arr2d, n=2):
    assert n>=2
    arr2d_sort = sorted(set(v for li in arr2d for v in li))
    return arr2d_sort[n-1]

def process(name, usefmt=True):
    import numpy as np
    matrix= np.load(name + ".npy")
    matrix= 100*matrix/matrix.sum()
    matrix= [[v.round(2) if v < 10 else v.round(1) for v in row] for row in matrix]

    plt.figure(figsize=(cm(15.6/3),cm(15.6/3)))
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major',
                   labelsize = 8)
    ax.tick_params(axis = 'both', which = 'minor',
                   labelsize = 8)
    [i.set_linewidth(0.1) for i in ax.spines.values()]
    if usefmt:
        g = sns.heatmap(matrix, vmax=nthmax(matrix, n=3), annot=True,
                    yticklabels=["CHAR", "FAC", "LOC", "O", "ORG", "PER"],
                    fmt='g',vmin=nthmin(matrix, 2),cbar=False,annot_kws={"fontsize":8})
    else:
        g = sns.heatmap(matrix, vmax=nthmax(matrix, n=3), annot=True,
                    yticklabels=["CHAR", "FAC", "LOC", "O", "ORG", "PER"],
                    vmin=nthmin(matrix, 2),cbar=False,annot_kws={"fontsize":8})
    g.set_yticklabels(g.get_yticklabels(), rotation = 0, fontsize = 8)
    plt.title(name, fontsize=10)
    plt.margins(x=0, y=0)

    plt.tight_layout()
    plt.savefig(name + ".png")
    plt.show()


process('conf_stanza', False)
process('conf_spacy')
process('conf_natasha')
