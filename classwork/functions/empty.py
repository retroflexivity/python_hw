def tillempty(prev):
    if (inp := input()):
        return(tillempty(prev + ' ' + inp))
    else:
        return(prev)

tillempty('')
