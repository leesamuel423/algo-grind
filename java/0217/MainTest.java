import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testContainsDuplicate() {
    Solution solution = new Solution();

    int [][] testCases = {
      {1, 2, 3, 1},
      {1, 2, 3, 4},
      {1, 2, 2, 3, 3, 4, 3, 2, 4, 2},
    };

    boolean[] expectedResults = {
      true,
      false,
      true
    };

    for (int i = 0; i < testCases.length; i++) {
      boolean result = solution.containsDuplicate(testCases[i]);
      assertEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
