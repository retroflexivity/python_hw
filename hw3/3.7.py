height = int(input())
weight = int(input())

if weight > (perfw := height - 100):
    print("Введенный вес -", weight, "- выше нормы, оптимальный вес -", perfw)
elif weight < perfw:
    print("Введенный вес -", weight, "- ниже нормы, оптимальный вес -", perfw)
else:
    print("Введенный вес -", weight, "- оптимален")
