import timeit
import functools

def mergeSort(tab):
    global equal
    global change_el
    if len(tab) > 1:
        mid = len(tab) // 2 
        lefthalf = tab[:mid]
        righthalf = tab[mid:]

        mergeSort(lefthalf) #sortowanie pierwszej połowy
        mergeSort(righthalf) #sortowanie drugiej połowy
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] > righthalf[j]:  #brak ostrności w nierówności powoduje stabilność algorytmu
                tab[k] = lefthalf[i]
                i = i + 1
                equal = equal + 1

                

            else:
                tab[k] = righthalf[j]
                j = j + 1
                equal = equal + 1
                change_el = change_el + 1
            k = k + 1

        # sprawdzdanie czy żaden element nie został opuszczony
        while i < len(lefthalf):
            tab[k] = lefthalf[i]

            i = i + 1
            k = k + 1

        while j < len(righthalf):
            tab[k] = righthalf[j]

            j = j + 1
            k = k + 1
    else:
        return tab

    #print("liczba operacji zamiany", equal)

if __name__== "__main__":

    size_tab = ''
    equal = 0
    change_el = 0
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
    #mergeSort(tab)
    t = timeit.Timer(functools.partial(mergeSort, tab))
    print(t.repeat(1,1))
    print("Ciąg wyjściowy", tab)
    print("liczba operacji porówań", equal)
    print("liczba operacji zamiany",change_el)



