class Solution(object):
    def isValid(self, s):
        # print(s)
        #loop thru each char in string
        #use split to turn the str into array list
        words = list(s)
        print(words)
        #loop thru the words array list, 
        #Use a stack of characters.
        stack = []
        #When you encounter an opening bracket, push it to the top of the stack.
        #When you encounter a closing bracket,
        # check if the top of the stack was the opening for it.        
        #Ifyes, pop it from the stack. Otherwise, return false.
        for char in words:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            #only reutnr True if the stack is empty for eadge cases
        if len(stack) == 0:
            return True
        else:
            return False
        
print(Solution().isValid("(]"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("()"))
print(Solution().isValid("("))
print(Solution().isValid("]"))
#this solution passes all leet code test cases