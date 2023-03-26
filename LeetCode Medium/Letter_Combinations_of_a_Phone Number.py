import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if len(digits) == 0:
            return combinations
        
        alphanumDic = {"2": ['a','b','c'],
                        "3": ['d','e','f'],
                        "4": ['g','h','i'],
                        "5": ['j','k','l'],
                        "6": ['m','n','o'],
                        "7": ['p','q','r','s'],
                        "8": ['t','u','v'],
                        "9": ['w','x','y','z']
                        }
        if len(digits) == 1:
            return alphanumDic[digits]
        keys = [i for i in digits]
        allLists = [alphanumDic[i] for i in keys]

        combinations = list( itertools.product(*allLists))
        maxLengthSubList = max(map(len,allLists))
        
        #combinations = combinations[:len(allLists[0]*maxLengthSubList)]
        combLength = len(combinations)
        for i in range(combLength):
            combinations[i] = ''.join(combinations[i])
        
        return combinations
