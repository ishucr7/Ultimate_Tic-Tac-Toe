from __future__ import print_function
import random
import copy
import datetime

INFINITY = 1e10

class Team47:

    def __init__(self):
        self.count = 0
        self.limit = 5
        self.termVal = INFINITY
        self.dict = {'x':1,'-':0,'d':0,'o':-1}
        self.weight = [3,2,2,3,2,3,3,2,2,3,3,2,3,2,2,3]
        self.total = {}
        self.timeLimit = datetime.timedelta(seconds = 2)
        self.begin = INFINITY
        self.limitReach = 0

    def evaluate(self,board,blx,bly,tmpBlock):
        # print("Calculating for block ",blx, " " , bly)
        # temp = board.block_status[blx][bly]
        # if(temp=='x' or temp=='o' or temp=='d'):
        #     return 0

        rowCnt = [3,3,3,3]
        colCnt = [3,3,3,3]
        val = 0
        for i in xrange(4):
            for j in xrange(4):
                temp = board.board_status[4*blx+i][4*bly+j]
                dictVal = self.dict[temp]
                if(dictVal!=0):
                    val+=dictVal*self.weight[4*i+j]
                    if (rowCnt[i]==3):
                        rowCnt[i] = dictVal*5
                    elif(dictVal*rowCnt[i]<0):
                        rowCnt[i] = 0
                    rowCnt[i]=rowCnt[i]*16
                    if (colCnt[j]==3):
                        colCnt[j] = dictVal*5
                    elif(dictVal*colCnt[j]<0):
                        colCnt[j] = 0
                    colCnt[j]=colCnt[j]*16
        # print(rowCnt,colCnt)

        diam1 = [3,3]       #diamond 1 and 2
        diam2 = [3,3]       #diamond 3 and 4

        for i in xrange(2):
            temp = board.board_status[4*blx][4*bly+1+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16
            temp = board.board_status[4*blx+1][4*bly+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16
            temp = board.board_status[4*blx+1][4*bly+2+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16
            temp = board.board_status[4*blx+2][4*bly+1+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16

        for i in xrange(2):
            temp = board.board_status[4*blx+1][4*bly+1+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16
            temp = board.board_status[4*blx+2][4*bly+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16
            temp = board.board_status[4*blx+2][4*bly+2+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16
            temp = board.board_status[4*blx+3][4*bly+1+i]
            dictVal = self.dict[temp]
            if(dictVal!=0):
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16


        draw = 12
        for i in xrange(4):
            if(colCnt[i]==0):
                draw-=1
            if(rowCnt[i]==0):
                draw-=1
        for i in xrange(2):
            if(diam1[i]==0):
                draw-=1
            if(diam2[i]==0):
                draw-=1

        if(draw==0):
            tmpBlock[blx][bly] = 'd'
            return 0

        for i in xrange(4):
            if(colCnt[i]!=3):
                val+=colCnt[i]
            if(rowCnt[i]!=3):
                val+=rowCnt[i]

        for i in xrange(2):
            if(diam1[i]!=3):
                val+=diam1[i]
            if(diam2[i]!=3):
                val+=diam2[i]

        return val

    def blockEval(self,board,tmpBlock):
        rowCnt = [3,3,3,3]
        colCnt = [3,3,3,3]
        val = 0
        for i in xrange(4):
            for j in xrange(4):
                temp = tmpBlock[i][j]
                dictVal = self.dict[temp]
                if(temp!='-'):
                    # print("Heuristic involves block ",i,j)
                    val+=dictVal*self.weight[4*i+j]
                    if (rowCnt[i]==3):
                        rowCnt[i] = dictVal*5
                    elif(dictVal*rowCnt[i]<=0):
                        rowCnt[i] = 0
                    rowCnt[i]=rowCnt[i]*16
                    if (colCnt[j]==3):
                        colCnt[j] = dictVal*5
                    elif(dictVal*colCnt[j]<=0):
                        colCnt[j] = 0
                    colCnt[j]=colCnt[j]*16

        diam1 = [3,3]       #diamond 1 and 2
        diam2 = [3,3]       #diamond 3 and 4

        for i in xrange(2):
            temp = tmpBlock[0][1+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<=0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16*dictVal*dictVal
            temp = tmpBlock[1][i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<=0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16*dictVal*dictVal
            temp = tmpBlock[1][2+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<=0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16*dictVal*dictVal
            temp = tmpBlock[2][1+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam1[i]==3):
                    diam1[i] = dictVal*5
                elif(dictVal*diam1[i]<=0):
                    diam1[i] = 0
                diam1[i]=diam1[i]*16*dictVal*dictVal

        for i in xrange(2):
            temp = tmpBlock[1][1+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<=0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16*dictVal*dictVal
            temp = tmpBlock[2][i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<=0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16*dictVal*dictVal
            temp = tmpBlock[2][2+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<=0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16*dictVal*dictVal
            temp = tmpBlock[3][1+i]
            if(temp!='-'):
                dictVal = self.dict[temp]
                if(diam2[i]==3):
                    diam2[i] = dictVal*5
                elif(dictVal*diam2[i]<=0):
                    diam2[i] = 0
                diam2[i]=diam2[i]*16*dictVal*dictVal

        for i in xrange(4):
            if(colCnt[i]!=3):
                val+=colCnt[i]
            if(rowCnt[i]!=3):
                val+=rowCnt[i]

        for i in xrange(2):
            if(diam2[i]!=3):
                val+=diam2[i]
            if(diam1[i]!=3):
                val+=diam1[i]

        # print("val is ",val)
        return val

    def heuristic(self, board):
        tmpBlock = copy.deepcopy(board.block_status)
        final_heur = 0
        # print("Calculating heur")
        for i in xrange(4):
            for j in xrange(4):
                best = self.evaluate(board,i,j,tmpBlock)
                # print(best,i,j)
                final_heur += best
        final_heur += self.blockEval(board,tmpBlock)*120
        del(tmpBlock)
        # return (50, old_move)
        # print("final_heur is ",final_heur)
        return final_heur

    def alphaBeta(self, board, old_move, flag, depth, alpha, beta):
        # Assuming 'x' to be the maximising player

        # print("old move is ",old_move)

        hashval = hash(str(board.board_status))
        if(self.total.has_key(hashval)):
            # print("hash exists")
            bounds = self.total[hashval]
            if(bounds[0] >= beta):
                return bounds[0],old_move
            if(bounds[1] <= alpha):
                return bounds[1],old_move
            # print("also returning")
            alpha = max(alpha,bounds[0])
            beta = min(beta,bounds[1])

        cells = board.find_valid_move_cells(old_move)
        random.shuffle(cells)
        # print(len(cells), ": length of cells")

        if (flag == 'o'):
            nodeVal = INFINITY, cells[0]
            new = 'x'
            temp = copy.deepcopy(board.block_status)
            b = beta

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                    # print("breaking")
                    self.limitReach = 1
                    break
                board.update(old_move, chosen, flag)
                # print("chosen ",chosen)
                if(board.find_terminal_state()[0] == 'o'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(temp)
                    nodeVal = -1*self.termVal,chosen
                    break
                elif(board.find_terminal_state()[0] == 'x'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(temp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE'):
                    # xprint("entering")
                    temp1 = 0
                    d = 0
                    x = 0
                    o = 0
                    # print("initialized")
                    for i2 in range(4):
                        for j2 in range(4):
                            if board.block_status[i2][j2] == 'x':
                                x += 1
                            if board.block_status[i2][j2] == 'o':
                                o += 1
                            if board.block_status[i2][j2] == 'd':
                                d += 1
                    # print("counted")
                    if(x==o):
                        temp1 = 0
                    elif(x<o):
                        temp1 = -INFINITY/2 - 10*(o-x)
                    else:
                        temp1 = INFINITY/2 + 10*(x-o)
                                            
                    # print(temp1)
                elif(depth >= self.limit):
                    temp1 = self.heuristic(board)
                    # print("Heuristic value for ",chosen," is ",temp1)
                else:
                    temp1 = self.alphaBeta(board, chosen, new, depth+1, alpha, b)[0]
                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(temp)
                if(nodeVal[0] > temp1):
                    nodeVal = temp1,chosen
                b = min(b, temp1)
                if alpha >= nodeVal[0] :
                    break
            del(temp)

        if (flag == 'x'):
            nodeVal = -INFINITY, cells[0]
            new = 'o'
            temp = copy.deepcopy(board.block_status)
            a = alpha

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                    # print("breaking at depth ",depth)
                    self.limitReach = 1
                    break
                board.update(old_move, chosen, flag)
                # print("chosen ",chosen)
                if (board.find_terminal_state()[0] == 'x'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(temp)
                    nodeVal = self.termVal,chosen
                    break
                elif (board.find_terminal_state()[0] == 'o'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(temp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE'):
                    # print("entering")
                    temp1 = 0
                    d = 0
                    o = 0
                    x = 0
                    # print("initialized")
                    for i2 in xrange(4):
                        for j2 in xrange(4):
                            if(board.block_status[i2][j2] == 'o'):
                                o += 1
                            if(board.block_status[i2][j2] == 'x'):
                                x += 1
                            if(board.block_status[i2][j2] == 'd'):
                                d += 1
                    # print("counted")
                    if(x==o):
                        temp1 = 0
                    elif(x<o):
                        temp1 = -INFINITY/2 - 10*(o-x)
                    else:
                        temp1 = INFINITY/2 + 10*(x-o)
                                            
                    # print(temp1)
                elif( depth >= self.limit):
                    temp1 = self.heuristic(board)
                    # print("Heuristic value for ",chosen," is ",temp1)
                else:
                    temp1 = self.alphaBeta(board, chosen, new, depth+1, a, beta)[0]

                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(temp)
                if(nodeVal[0] < temp1):
                    nodeVal = temp1,chosen
                # print("hi nodeval ",nodeVal)
                a = max(a, temp1)
                if beta <= nodeVal[0] :
                    break
            del(temp)

        # print("return value is ",nodeVal)
        if(nodeVal[0]>=beta):
            self.total[hashval] = [nodeVal[0],INFINITY]
        if(nodeVal[0] > alpha and nodeVal[0] < beta):
            self.total[hashval] = [nodeVal[0],nodeVal[0]]
        if(nodeVal[0] <= alpha):
            self.total[hashval] = [-INFINITY,nodeVal[0]]

        # print(self.total.items())
        return nodeVal

    def minimax(self,board,old_move,flag,depth,f):
        g = f
        lowerbound = -INFINITY
        upperbound = INFINITY
        while(lowerbound<upperbound):
            # print("new minimax ",lowerbound,upperbound)
            b = max(g,lowerbound+1)
            temp = self.alphaBeta(board,old_move,flag,depth,b-1,b)
            if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                # print("breaking_end")
                self.limitReach = 1
                break
            g = temp[0]
            # print(g)
            if(g>b):
                lowerbound = g
            else:
                upperbound = g       
        return temp

    def move(self, board, old_move, flag):
        # print("hey")
        self.begin = datetime.datetime.utcnow()
        self.count += 1
        self.limitReach = 0
        self.total.clear()
        # print(self.total.items())
        # print("entering the move for ", self.count)
        best_move = board.find_valid_move_cells(old_move)[0]
        for i in xrange(3,100):
            self.total.clear()
            self.limit = i
            # print("in depth ",i)
            best = self.alphaBeta(board, old_move, flag, 1, -INFINITY, INFINITY)
            getval = best[1]
            #print("Returning finally ",best[0])
            #print("returned from depth ",i)
            if(self.limitReach == 0):
                best_move = getval
            else:
                break
        # best_move = self.alphaBeta(board, old_move, flag, 1, -10000000, 10000000)[1]
        # print("best_move",best_move)
        return best_move[0], best_move[1]
