import re
from pprint import pprint
List = [
'Chevrolet Camaro О123ЕХ777 #C222ЕЕ120У33',
'Chevrolet Impala О456ЕР199 #C345ЕЕ120У33',
'Chevrolet Malibu С789НХ797, #Н777ОХ220Р44',
'Chevrolet Tahoe К321РО177, #Р123ОУ100К22',
'Chevrolet Equinox У654ОУ799, #С678УХ450Н11',
'Chevrolet Traverse О987РЕ797, #Е234КС650Х55',
'Chevrolet Silverado Е456СР799, #Р678СО120Н22',]

pattern = '([А-я])\s*(\d{3})\s*([А-я]{2})\s*(\d+\S+)'
L = []
for i in List:
    result = re.finditer(pattern, i)
    L.append([i[0] for i in result])
pprint(L)

    
    
 