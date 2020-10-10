class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
              
        # Sort String first
        # check same string on length        
        ans = collections.defaultdict(list)
        
        for s in strs:
            tuples = tuple(sorted(s))
            ans[tuples].append(s)
        return list(ans.values())
            
    # Dictionary를 쓰면 Key Valu로 나뉘게 된다. 
    # 먼저 Sorting을 한 다음에, 그 Sorting한 문자를 기준으로, Key를 설정해두고
    # 각 Value들을 그 Key에 맞게 끼워 넣는다. 
    
    