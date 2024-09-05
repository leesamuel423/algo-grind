import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void getConcatenation() {
    Solution solution = new Solution();

    int[][] testCasesNums = {
      {1, 2, 1},
      {1, 3, 2, 1}
    };

    int[][] expectedResults = {
      {1, 2, 1, 1, 2, 1},
      {1, 3, 2, 1, 1, 3, 2, 1},
    };

    for (int i = 0; i < testCasesNums.length; i++) {
      int[] result = solution.getConcatenation(testCasesNums[i]);
      assertArrayEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
