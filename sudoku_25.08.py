sudoku_grid = [
    [0, 0, 2, 4, 0, 6, 3, 0, 0],
    [3, 0, 8, 9, 1, 0, 6, 0, 4],
    [6, 0, 1, 0, 0, 0, 0, 0, 2],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 9, 2, 8, 0, 5, 0, 6],
    [0, 0, 5, 6, 0, 3, 0, 7, 8],
    [9, 0, 3, 5, 0, 0, 0, 0, 7],
    [0, 1, 0, 0, 6, 0, 0, 3, 0],
    [2, 0, 0, 0, 4, 1, 8, 6, 0]
]
def affichage(grille):#affiche la grille
    for line in grille:
        print(line)
def ligne(iL):#renvoie les chiffres possibles dans la ligne
    return(sudoku_grid[iL])
def colonne(iC):#renvoie les chiffres possibles dans la colonne
    colonne=[]
    for ind in range(9):
        colonne.append(sudoku_grid[ind][iC])
    return(colonne)
def cube(iL,iC):#renvoie les chiffres possibles dans le cube
    cub=[]
    maxL,maxC=iL%3,iC%3
    for l in range(iL-maxL,iL+3-maxL):
        for c in range(iC - maxC, iC + 3 - maxC):
            cub.append(sudoku_grid[l][c])
    return(cub)
def possibleE(iL,iC):#renvoie les chiffres possibles a cet emplacement
    possible=[]
    liste=ligne(iL)+colonne(iC)+cube(iL,iC)
    for num in range(1,10):
        if num not in liste:
            possible.append(num)
    return(possible)

def possibleL(iL,iC):#renvoie les chiffres possible aux autres emplacements de la ligne
    liste=[]
    for i in range(9):
        if sudoku_grid[iL][i]==0 and i!=iC:
            liste.extend(possibleE(iL,i))
    return(liste)

def possibleC(iL,iC):#renvoie les chiffres possible aux autres emplacements de la colonne
    liste=[]
    for i in range(9):
        if sudoku_grid[i][iC]==0 and i!=iL:
            var = possibleE(i,iC)
            liste.extend(var)
    return(liste)

def possibleCube(iL,iC):#renvoie les chiffres possible aux autres emplacements du cube
    liste=[]
    maxL,maxC=iL-iL%3,iC-iC%3
    for i in range(maxL,maxL+3):
        for j in range(maxC,maxC+3):
            if sudoku_grid[i][j]==0 and (iL,iC)!=(i,j):
                liste.extend(possibleE(i,j))
    return(liste)

def estPlein(grille):#verifie si la grille est pleine
    for line in grille:
        if 0 in line:
            return(False)
    return(True)
def main():#fonction principale
    print('-----Grille de base-----')
    affichage(sudoku_grid)
    while not estPlein(sudoku_grid):
        for iL in range(9):
            for iC in range(9):
                element=sudoku_grid[iL][iC]
                if element==0:
                    a = possibleE(iL,iC) #combinaisons possible a l'emplacment iL,iC
                    b = possibleL(iL,iC) #combinaisons possible sur la ligne iL
                    c = possibleC(iL,iC) #combinaisons possible sur la colonne iC
                    d = possibleCube(iL,iC) #combinaisons possible dans le cube iL,iC
                    for element in a: #verifie si il y a des elements propre à a
                        if element not in b or element not in c or element not in d:
                            sudoku_grid[iL][iC]=element
    print('\n', '-----Grille résolue-----')
    affichage(sudoku_grid)

main()
