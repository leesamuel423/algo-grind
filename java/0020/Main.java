import java.util.*;

class Solution {
  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();

    HashMap<Character, Character> dict = new HashMap<>();
    dict.put(')', '(');
    dict.put(']', '[');
    dict.put('}', '{');

    for (char el : s.toCharArray()) {
      if (dict.containsKey(el)) {
        if (stack.isEmpty()) return false;
        if (!dict.get(el).equals(stack.pop())) return false;
      } else {
        stack.push(el);
      }
    }
    
    return stack.isEmpty();
  }
}
