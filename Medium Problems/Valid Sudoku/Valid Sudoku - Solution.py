class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        boxMap = {"b1": [], "b2": [], "b3": [], "b4": [], "b5": [], "b6": [], "b7": [], "b8": [], "b9": []}
        rowMap = {}
        colMap = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != "."):
                    if(i not in rowMap):
                        rowMap[i] = [board[i][j]]
                    else:
                        rowMap[i].append(board[i][j])
                        
                    if(j not in colMap):
                        colMap[j] = [board[i][j]]
                    else:
                        colMap[j].append(board[i][j])
                        
                    if(i <= 2):
                        if(j <= 2):
                            #b1
                            boxMap["b1"].append(board[i][j])
                        elif(j <= 5):
                            #b2
                            boxMap["b2"].append(board[i][j])
                        else:
                            #b3
                            boxMap["b3"].append(board[i][j])
                    elif(i <= 5):
                        if(j <= 2):
                            #b4
                            boxMap["b4"].append(board[i][j])
                        elif(j <= 5):
                            #b5
                            boxMap["b5"].append(board[i][j])
                        else:
                            #b6
                            boxMap["b6"].append(board[i][j])
                    else:
                        if(j <= 2):
                            #b7
                            boxMap["b7"].append(board[i][j])
                        elif(j <= 5):
                            #b8
                            boxMap["b8"].append(board[i][j])
                        else:
                            #b9
                            boxMap["b9"].append(board[i][j])
                            
        rowsList = list(rowMap.values())
        colsList = list(colMap.values())
        boxesList = list(boxMap.values())
        
        print("ROWS")
        print(rowsList)
        
        print("COLS")
        print(colsList)
        
        print("BOXES")
        print(boxesList)
        
        for i in rowsList:
            for j in range(len(i)-1):
                i = sorted(i)
                if(i[j] == i[j+1]):
                    return False
                
        for i in colsList:
            for j in range(len(i)-1):
                i = sorted(i)
                if(i[j] == i[j+1]):
                    return False
        
        for i in boxesList:
            for j in range(len(i)-1):
                i = sorted(i)
                if(i[j] == i[j+1]):
                    return False
                
        return True
                
        