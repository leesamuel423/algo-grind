#include "cpp/0020/solution.h"
#include <gtest/gtest.h>

TEST(IsValid, Test1) {
  Solution solution;
  std::string test = "()";
  EXPECT_TRUE(solution.isValid(test));
}

TEST(IsValid, Test2) {
  Solution solution;
  std::string test = "()[]{}";
  EXPECT_TRUE(solution.isValid(test));
}
TEST(IsValid, Test3) {
  Solution solution;
  std::string test = "(]";
  EXPECT_FALSE(solution.isValid(test));
}

TEST(IsValid, Test4) {
  Solution solution;
  std::string test = "([])";
  EXPECT_TRUE(solution.isValid(test));
}

TEST(IsValid, Test5) {
  Solution solution;
  std::string test = "([)]";
  EXPECT_FALSE(solution.isValid(test));
}
