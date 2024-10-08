import java.util.*;

public class Solution {

  private Stack<Integer> stack;
  private Stack<Integer> minStack;

  public Solution() {
    stack = new Stack<>();
    minStack = new Stack<>();
  }

  public void push(int x) {
    stack.push(x);
    if (minStack.isEmpty()) {
      minStack.push(x);
    } else {
      minStack.push(Math.min(x, minStack.peek()));
    }
  }

  public void pop() {
    stack.pop();
    minStack.pop();
  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return minStack.peek();
  }
}
