import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testIsValid() {
    Solution solution = new Solution();

    String[] testCasesNums = {
      "()",
      "()[]{}",
      "(]",
      "([])",
      "([)]"
    };

    boolean[] expectedResults = {
      true,
      true,
      false,
      true,
      false
    };

    for (int i = 0; i < testCasesNums.length; i++) {
      boolean result = solution.isValid(testCasesNums[i]);
      assertEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
