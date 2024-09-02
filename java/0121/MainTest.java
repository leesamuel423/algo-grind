import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testMaxProfit() {
    Solution solution = new Solution();

    int[][] testCases = {
      {7, 1, 5, 3, 6, 4},
      {7, 6, 4, 3, 1}
    };

    int[] expectedResults = {
      5,
      0
    };

    for (int i = 0; i < testCases.length; i++) {
      int result = solution.maxProfit(testCases[i]);
      assertEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
