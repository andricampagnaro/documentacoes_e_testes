class MeusLayouts:
    def __init__(self):
        self.layouts = ['smart_01_10', 'smart_01_11', 'smart_01_12']

    def __iter__(self):
        for layout in self.layouts:
            yield layout

lista_layouts = MeusLayouts()
for i in lista_layouts:
    print(i)

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
lista1.extend(lista2)
print(lista1)