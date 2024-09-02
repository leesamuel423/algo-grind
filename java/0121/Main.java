class Solution {
  public int maxProfit(int[] prices) {
    int minimum = Integer.MAX_VALUE;
    int maximum = 0;

    for (int i = 0; i < prices.length; i++) {
      if (prices[i] < minimum) {
        minimum = prices[i];
      } else if (prices[i] - minimum > maximum) {
        maximum = prices[i] - minimum;
      }
    }

    return maximum;
  }
}
