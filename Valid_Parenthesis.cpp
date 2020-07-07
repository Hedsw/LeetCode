// Close parentheses are always before open parentheses. 
class Solution {
public:
    bool isValid(string s) {
        stack<char> mystack; 
        
        if(s.size() % 2 == 1 || s[0] == ')' || s[0] == '}' || s[0] == ']') return false;
        if(s.empty()) return true;
        
        for(char c : s) {
            switch (c) {
                case '(':  
                case '{':
                case '[': mystack.push(c); break;
                case '}': if(mystack.top() != '{') return false; else mystack.pop(); break; 
                case ')': if(mystack.top() != '(') return false; else mystack.pop(); break;
                case ']': if(mystack.top() != '[') return false; else mystack.pop(); break;
            }   
        }  
        return mystack.empty();
    }
};

