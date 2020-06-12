import timeit
import functools

def shellSort(arr): 
    z = 0 # liczba zmian
    p = 0 # liczba porównań jest to w tym momencie ilość przejść przez pętlę for plus wejścia w pętlę while w środku
    
    n = len(arr) 
    gap = n//2
  
    
    while gap > 0: 
  
        for i in range(gap,n):             
            currentvalue = arr[i]             
            j = i # zindeks
            while  j >= gap and arr[j-gap] <currentvalue: # kiedy ilość liczb jest nieparzysta, to przeleci 2 razy
                arr[j] = arr[j-gap] 
                j -= gap      
                z += 1      
                p +=1
            arr[j] = currentvalue 
            p += 1
        print("przyrost: ", gap)
        gap //= 2
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
    print("Ciąg wejściowy", tab)
    # print(quicksort(tab))
    # print("Ciąg wyjciowy", shellSort(tab))
    # print("liczba operacji porówań", por)
    # print('liczba zmian',zm)
    t = timeit.Timer(functools.partial(shellSort, tab)) # do mierzenia czasu tysiac razy
    print(t.repeat(1,1))
    print("Ciąg wyjciowy", tab)