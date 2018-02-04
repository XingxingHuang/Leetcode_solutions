# https://leetcode.com/problems/sliding-puzzle/description/
import timeit

class Solution:
    def slidingPuzzle(self, board):
        state = "".join([str(n) for row in board for n in row])
        ans = "123450"
        if state ==ans:
            return 0

        mem = set()
        mem.add(state)
        # remember steps count in the queue
        queue = [(state,0)]

        # specify four swap conditions
        conditions = [
                (lambda x: x-1>=0 and x !=3, -1),
                (lambda x: x-3>=0 ,          -3),
                (lambda x: x+1< 6 and x !=2, 1),
                (lambda x: x+3< 6 ,          3)]

        while queue:
            state, step= queue.pop(0)
            zp = state.find('0')
            for c in conditions:
                if c[0](zp):
                    # swap
                    nstate= [s for s in state]
                    nstate[zp],nstate[zp+c[1]]=nstate[zp+c[1]],nstate[zp]
                    nstate= "".join(nstate)

                    if nstate ==ans:
                        return step+1
                    if nstate not in mem:
                        mem.add(nstate)
                        queue.append((nstate,step+1))
        return -1

def run():
    board = [[4,1,2],[5,0,3]]
    Solution().slidingPuzzle(board)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
