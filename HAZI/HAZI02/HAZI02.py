# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
#(1) Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(arr : np.array) -> np.array:
    arr[:, [0,1]] = arr[:, [1, 0]]
    return arr

#column_swap(np.array([[1,2],[3,4]]))

# %%
#(2) Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(arr1 : np.array, arr2 : np.array) -> np.array:
    return np.where(arr1[:] == arr2[:])[0]

''' array([1, 3], dtype=int64)'''
#compare_two_array(np.array([7,8,9, 10]), np.array([9,8,7, 10]))

# %%
#(3) Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 

def get_array_shape(arr : np.array)->np.array:
    if len(np.shape(arr)) == 3:
        return f"sor: {np.shape(arr)[0]}, oszlop: {np.shape(arr)[1]}, melyseg: {np.shape(arr)[2]}"
    else:
        return f"sor: {np.shape(arr)[0]}, oszlop: {np.shape(arr)[1]}, melyseg: 1"

#get_array_shape(np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]))
#get_array_shape(np.array([[1,2,3], [4,5,6]]))

# %%
#(4) Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(arr : np.array, n : int)-> np.array:
    temp_arr = np.zeros((np.shape(arr)[0], n))
    temp_arr[np.arange(n), arr[:]] = 1
    return temp_arr


#encode_Y([1, 2, 0, 3], 4)

# %%
#(5) A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(arr:np.array)-> np.array:
    return np.where(arr == 1)[1]


'''eredmény: array([1, 2, 0, 3], dtype=int64) '''
#decode_Y(np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]))

# %%
#(6) Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

def eval_classification(input_list : list, arr : np.array)-> str:

    return input_list[np.argmax(arr)]


#eval_classification(['alma', 'körte', 'szilva', 'kaga', 'banab'], np.array([0.2, 0.2, 0.6, 0.6, 1]))

# %%
#(7) Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

def repalce_odd_numbers(arr : np.array)-> np.array:
    arr[np.where(arr % 2 == 1)] = -1
    return arr

#repalce_odd_numbers(np.array([1,2,3,4,5,6]))

# %%
#(8) Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

def replace_by_value(arr : np.array, i : int)-> np.array:
    arr[arr < i] = -1
    arr[arr >= i] = 1

    return arr

replace_by_value(np.array([1, 2, 5, 0]), 2)


# %%
#(9) Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

def array_multi(arr : np.array)-> int:

    return np.prod(arr)

#array_multi(np.array([1,2,3,4]))

# %%
#(10) TODO Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

def array_multi_2d(arr : np.array)-> np.array:
    temp_arr = np.arange(np.shape(arr)[0])
    temp_arr[:] = np.prod(arr[:])

    i = 0
    return temp_arr


#array_multi_2d(np.array([[1, 2], [3, 4]]))

# %%
#(11) Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()

def add_border(arr : np.array)-> np.array:
    return np.pad(arr, pad_width=1)

#add_border(np.array([[1,2],[3,4]]))


# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
#(12) Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

def list_days(date1: str, date2: str)-> np.array:
    return np.arange(date1, date2, dtype='datetime64[D]')

#list_days('2023-02', '2023-04')
# %%
#(13) Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24
#get_act_date():

def get_act_date()-> np.datetime64():
    return np.datetime64()


# %%
#(14) Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()


