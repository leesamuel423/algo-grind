import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testMinStack() {
    String[] operations = {"MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"};
    int[][] arguments = {{}, {-2}, {0}, {-3}, {}, {}, {}, {}};
    Object[] expected = {null, null, null, null, -3, null, 0, -2};

    Solution s = new Solution();
    Object[] actual = new Object[operations.length];

    for (int i = 0; i < operations.length; i++) {
      switch (operations[i]) {
        case "MinStack":
        // MinStack constructor already invoked, nothing to do here
        actual[i] = null;
        break;
        case "push":
        s.push(arguments[i][0]);
        actual[i] = null;
        break;
        case "pop":
        s.pop();
        actual[i] = null;
        break;
        case "top":
        actual[i] = s.top();
        break;
        case "getMin":
        actual[i] = s.getMin();
        break;
      }
    }

    assertArrayEquals(expected, actual);
  }
}
