import timeit
import functools
def shellSort2(arr): 
    z = 0 # liczba zmian
    p = 0 # liczba porównań jest to w tym momencie ilość przejść przez pętlę for plus wejścia w pętlę while w środku
    k = 1 # etap
    n = len(arr) 
    d = 1 # krok

    while d<n/3:
        d = 3*d + 1
  
    
    while d > 0: 
  
        for i in range(d,n):             
            temp = arr[i]             
            j = i # zapisujemy by potem zamienić
            while  j >= d and arr[j-d] <temp: 
                arr[j] = arr[j-d] 
                j -= d      
                z += 1      
                p +=1
            arr[j] = temp 
            p += 1
        print('przyrost ',d)
        d -= 1
        
        d = d//3 
        
    print('liczba zmian ',z)
    print('liczba porownan ',p)
    return arr


if __name__== "__main__":

    size_tab = ''
    por = 0
    zm = 0
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
    timetab = tab
    print("Ciąg wejściowy", tab)
    # print(quicksort(tab))
    # print("Ciąg wyjściowy", shellSort2(tab)) #!!!!!
    # print("liczba operacji porówań", por)
    # print('liczba zmian',zm)
    t = timeit.Timer(functools.partial(shellSort2, tab)) # do mierzenia czasu tysiac razy
    print(t.repeat(1,1))
    print(tab)