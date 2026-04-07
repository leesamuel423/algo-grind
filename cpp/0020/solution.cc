#include "solution.h"

#include <map>
#include <stack>

using namespace std;

bool Solution::isValid(string s) {
  stack<char> stack;
  map<char, char> dict = {
      {')', '('},
      {']', '['},
      {'}', '{'},
  };

  for (char el : s) {
    if (dict.count(el)) {
      if (stack.empty())
        return false;
      if (dict[el] != stack.top())
        return false;
      stack.pop();
    } else {
      stack.push(el);
    }
  }

  return stack.empty();
}
