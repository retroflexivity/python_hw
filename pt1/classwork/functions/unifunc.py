def foo(list, arg='all'):
    match arg:
        case 'rev':
            out = []
            for item in list:
                out = [item] + out
            return(out)

        case 'len':
            i = 0
            for item in list:
                i += 1
            return i

        case 'max':
            max = list[0]
            for item in list[1:]:
                if item > max:
                    max = item
            return max

        case 'all':
            return (foo(list, 'rev'), foo(list, 'len'), foo(list, 'max'))


print(foo([1, 3, 5, 4, -1, 0]))
