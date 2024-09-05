#ifndef SOLUTION_H
#define SOLUTION_H

#include <iostream>
#include <vector>
#include <stack>
#include <map>

using namespace std;

class Solution {
public:
  bool isValid(string s) {
    stack<char> stack;
    map<char, char> dict = {
      {')','('},
      {']','['},
      {'}','{'},
    };

    for (char el : s) {
      if (dict.count(el)) {
        if (stack.empty()) return false;
        if (dict[el] != stack.top()) return false;
        stack.pop();
      } else {
        stack.push(el);
      }
    }

    return stack.empty();
  }
};


#endif // SOLUTION_H
