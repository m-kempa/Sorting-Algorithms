import timeit
import functools

def quicksort(zbior):
    left = []
    right = []
    l = [] # lista środkowa
    global equal
    global swap 
    hah = 0 #warunek pojedynczego wejścia
    if len(zbior) > 1:
        
        pivot = zbior[0]
        for x in zbior:
            if hah == 0:
                l.append(x)
                hah += 1        
            elif x == pivot:
                l.append(x)
                equal += 1            # pierwszy if z hah nie jest porównaniem i zaburzał wyniki
            elif x > pivot:
                left.append(x)
                swap += 1
                equal += 1
            else :
                right.append(x)
                equal += 1
            
        print ('dla pivota ',pivot,)
        
        return quicksort(left)+l+quicksort(right)  
    
    else:          
        return zbior

def ssort(t):
    global tab 
    tab = quicksort(t)
    return t


if __name__== "__main__":

    size_tab = ''
    swap = 0
    equal = 0
    
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
    # print(quicksort(tab))
    # print("Ciąg wyjściowy", quicksort(tab))
    # print("liczba operacji porówań", por)
    # print('liczba zmian',zm)
    
    t = timeit.Timer(functools.partial(ssort, tab)) # do mierzenia czasu tysiac razy
    print(t.repeat(1,1))
    print("Ciag wyjsciowy ",tab)      # działa bez czasu
    print ('liczba zmian ',swap)
    print ('liczba porownan',equal)



    