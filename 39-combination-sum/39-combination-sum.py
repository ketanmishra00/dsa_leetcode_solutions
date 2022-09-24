class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        ret = []
        
        stack.append((candidates, target, []))
        while stack:
            curr_set,curr_target,path = stack.pop()
            print(curr_set)
            if curr_target < 0:
                pass
            elif curr_target == 0:
                ret.append(path)
            else:
                for i in range(len(curr_set)):
                    stack.append((curr_set[i:], curr_target-curr_set[i], path+[curr_set[i]]))
        return ret