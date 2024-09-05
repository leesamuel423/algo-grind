#include <gtest/gtest.h>
#include "cpp/1929/solution.h"

TEST(GetConcatenation, Test1) {
  Solution solution;
  std::vector<int> nums = {1, 2, 1};
  std::vector<int> expected = {1, 2, 1, 1, 2, 1};
  EXPECT_EQ(solution.getConcatenation(nums), expected);
}

TEST(GetConcatenation, Test2) {
  Solution solution;
  std::vector<int> nums = {1, 3, 2, 1};
  std::vector<int> expected = {1, 3, 2, 1, 1, 3, 2, 1};
  EXPECT_EQ(solution.getConcatenation(nums), expected);
}

TEST(GetConcatenation, Test3) {
  Solution solution;
  std::vector<int> nums = {3, 3};
  std::vector<int> expected = {3, 3, 3, 3};
  EXPECT_EQ(solution.getConcatenation(nums), expected);
}
