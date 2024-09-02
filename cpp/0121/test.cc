#include <gtest/gtest.h>
#include "cpp/0121/solution.h"

TEST(MaxProfitTest, Test1) {
  Solution solution;
  std::vector<int> nums = {7, 1, 5, 3, 6, 4};
  EXPECT_EQ(solution.maxProfit(nums), 5);
}

TEST(MaxProfitTest, Test2) {
  Solution solution;
  std::vector<int> nums = {7, 6, 4, 3, 1};
  EXPECT_EQ(solution.maxProfit(nums), 0);
}
