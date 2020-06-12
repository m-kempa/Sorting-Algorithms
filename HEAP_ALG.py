import timeit
import functools

#funkcja żeby stworzyć podrzewo w indekcjie i. n to wielkosc stosu
def parents(arr, n, i):
    global equal
    global swap
    largest = i  # jako korzen
    l_child = 2 * i + 1  # lewe = 2*i + 1
    r_child = 2 * i + 2  # prawe = 2*i + 2

    # sprawdzamy czy istnieje lewe dziecko korzenia mniejsze niż korzen
    if l_child < n and arr[i] > arr[l_child]:
        largest = l_child
        equal += 1

    # prawdzamy czy istnieje prawe dziecko korzenia mniejsze niż korzen
    if r_child < n and arr[largest] > arr[r_child]:
        largest = r_child
        equal += 1

        # Jeśli trzeba, zmieniamy korzeń
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swap = swap + 1

        #stosujemy funkcje do korzenia
        parents(arr, n, largest)



def heapSort(arr):
    n = len(arr)
    global swap
    # budowanie maksymalnego stosu
    for i in range(n, -1, -1):
        parents(arr, n, i)

    # wyodrębnianie kolejnych elementów
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   #zamiana korzenia z "ostatnim dzieckiem"
        #swap = swap + 1
        parents(arr, i, 0)


if __name__== "__main__":

    size_tab = ''
    equal = 0
    swap = 0
    
    while size_tab.isdigit() == False:
            size_tab = input("podaj wielkosc tablicy nie wieksza niz 10 ")
            
    
    size_tab = int(size_tab)
    while size_tab > 10 or size_tab == 0:
        size_tab = input("podaj wielkosc tablicy nie wieksza niz 10 ")
        

    tab = []
    i = 0
    while i < size_tab:
        element = input("podaj {} wartosc tablicy ".format(i + 1))
        if element.isdigit():
            tab.append(int(element))
            i = i + 1
        else:
            print("Podane nade sa nieprawidlowe")
    print("Ciąg wejściowy", tab)
    t = timeit.Timer(functools.partial(heapSort, tab))
    print(t.repeat(1,1))
    print("Ciąg wyjściowy", tab)
    print("Liczba operacji porównań", equal)
    print("Liczba operacji zamiany", swap)