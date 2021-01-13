class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        
        if(len(strs) == 1):
            return strs[0]
        
        minStr = 999999
        
        for j in strs:
            if(len(j) < minStr):
                minStr = len(j)
                
        keyStr = strs[0]
        prefix = ""
        
        i = 0
        
        while(i < minStr):
            flag = True
            keyChr = keyStr[i]
            
            for k in strs:
                if(k[i] != keyChr):
                    flag = False
                    return prefix
            
            if(flag == True):
                prefix = prefix + keyChr
            i = i + 1
            
        return prefix
        