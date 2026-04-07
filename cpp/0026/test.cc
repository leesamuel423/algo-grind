#include "cpp/0026/solution.h"
#include <gtest/gtest.h>

TEST(RemoveDuplicatesTest, BasicDuplicates) {
  Solution solution;
  std::vector<int> nums = {1, 1, 2};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 2);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{1, 2}));
}

TEST(RemoveDuplicatesTest, ManyDuplicates) {
  Solution solution;
  std::vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 5);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{0, 1, 2, 3, 4}));
}

TEST(RemoveDuplicatesTest, EmptyArray) {
  Solution solution;
  std::vector<int> nums = {};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 0);
}

TEST(RemoveDuplicatesTest, SingleElement) {
  Solution solution;
  std::vector<int> nums = {42};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 1);
  EXPECT_EQ(nums[0], 42);
}

TEST(RemoveDuplicatesTest, AllIdentical) {
  Solution solution;
  std::vector<int> nums = {7, 7, 7, 7, 7};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 1);
  EXPECT_EQ(nums[0], 7);
}

TEST(RemoveDuplicatesTest, AlreadyUnique) {
  Solution solution;
  std::vector<int> nums = {1, 2, 3, 4, 5};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 5);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{1, 2, 3, 4, 5}));
}

TEST(RemoveDuplicatesTest, NegativeNumbers) {
  Solution solution;
  std::vector<int> nums = {-3, -3, -1, 0, 0, 0, 2};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 4);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{-3, -1, 0, 2}));
}

TEST(RemoveDuplicatesTest, TwoElements) {
  Solution solution;
  std::vector<int> nums = {1, 1};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 1);
  EXPECT_EQ(nums[0], 1);
}

TEST(RemoveDuplicatesTest, TwoDistinct) {
  Solution solution;
  std::vector<int> nums = {1, 2};
  int k = solution.removeDuplicates(nums);
  EXPECT_EQ(k, 2);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{1, 2}));
}
