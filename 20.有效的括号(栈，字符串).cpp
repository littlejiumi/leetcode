class Solution {
public:
    stack<char> st;   //定义栈
    bool isValid(string s) {
        for(int i = 0; i < s.size(); i++){
            if(st.empty()) st.push(s[i]);
            else if(st.top() == '(' && s[i] == ')') st.pop();
            else if(st.top() == '[' && s[i] == ']') st.pop();
            else if(st.top() == '{' && s[i] == '}') st.pop();
            else st.push(s[i]);
        }
        return st.empty();  //防止最后剩括号
    }
};
