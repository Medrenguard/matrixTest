import random, re, copy as cp
print("Матрица состоит из нулей и единиц. Найдите в ней самую длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.\n")
  
n = random.randint(3,7)
m = random.randint(3,7)
 
def printArr(arr):
    for row in arr:
        s = ''
        for item in row:
            s+= str(item).center(4)
        print(s)
    print('\n')

array = [[random.randint(0,1) for i in range(m)]for t in range(n)]
printArr(array)

def searchChains(arr):
    def SCFE(arr, el, res):  # search chain from element
        chainsFE = [el]  # chains from element; включая одиночный элемент
        curChain = [el]  # включая стартовый элемент
        arl = [len(arr), len(arr[0])]  # array length

        ways = {'t': [[-1, 0]],     # индексы сторон, в которые может осуществляться поиск
                'r': [[0, 1]],      # перечислены по часовой стрелке, начиная с самого старого "часа"
                'b': [[1, 0]],      # кроме полного круга trbl.
                'l': [[0, -1]],     # trbl начинается с классического 1 (правый верх)
                'tr': [[-1, 0], [-1, 1], [0, 1]],
                'tl': [[0, -1], [-1, -1], [-1, 0]],
                'br': [[0, 1], [1, 1], [1, 0]],
                'bl': [[1, 0], [1, -1], [0, -1]],
                'brl': [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1]],
                'tbl': [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]],
                'trl': [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]],
                'tbr': [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]],
                'tbrl': [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]}

        dir = 'tbrl'  # начальные направления поиска для конкретного элемента
        if el[0] == 0: dir = re.sub('t', '', dir)
        if el[0] == arl[0]-1: dir = re.sub('b', '', dir)
        if el[1] == 0: dir = re.sub('l', '', dir)
        if el[1] == arl[0]-1: dir = re.sub('r', '', dir) #пожалуй, лучше битовая маска. Но это еще функцию для чтения по ней писать..

        # перебираем возможные направления
        for g in ways[dir]:
            i = 1
            nextUnit = [el[0] + g[0]*i, el[1] + g[1]*i]
            # перебираем очередь совпадений
            while nextUnit[0]//n == nextUnit[1]//m == 0 and arr[nextUnit[0]][nextUnit[1]] == 0:
                curChain.append([nextUnit[0], nextUnit[1]])
                i += 1
                nextUnit = [el[0] + g[0]*i, el[1] + g[1]*i]
            # если текущая цепь больше стандартной и в итоговом пуле нет его вариаций, расчитанных с другой ячейки
            if len(curChain) > 1 and not res.count(curChain[::-1]): 
                chainsFE.append(curChain)
            curChain = [el]

        return chainsFE

    ##//////////////##

    allChains = []
    maxLenChain = 0
    maxChains = []
    for i in range(n):
        for r in range(m):
            if arr[i][r] == 0: 
                allChains += SCFE(arr, [i, r], allChains)
    
    for chain in allChains:
        if len(chain) >= maxLenChain:
            if len(chain) > maxLenChain:
                maxLenChain = len(chain)
                maxChains = []
            maxChains.append(chain)

    return [maxLenChain, maxChains]

res = searchChains(array)
print('Максимальных цепочек обнаружено: {}, длина {} знака(ов).\n'.format(len(res[1]), res[0]))
for i in range(len(res[1])):
    print('Цепочка №', i+1)
    var = cp.deepcopy(array)
    for r in range(len(res[1][i])):
        var[res[1][i][r][0]][res[1][i][r][1]] = '!*!'
    printArr(var)
