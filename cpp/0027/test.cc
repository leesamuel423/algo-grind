#include "cpp/0027/solution.h"
#include <algorithm>
#include <gtest/gtest.h>

TEST(RemoveElementTest, BasicRemoval) {
  Solution solution;
  std::vector<int> nums = {3, 2, 2, 3};
  int k = solution.removeElement(nums, 3);
  EXPECT_EQ(k, 2);
  std::sort(nums.begin(), nums.begin() + k);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{2, 2}));
}

TEST(RemoveElementTest, MixedValues) {
  Solution solution;
  std::vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
  int k = solution.removeElement(nums, 2);
  EXPECT_EQ(k, 5);
  std::sort(nums.begin(), nums.begin() + k);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{0, 0, 1, 3, 4}));
}

TEST(RemoveElementTest, AllMatch) {
  Solution solution;
  std::vector<int> nums = {1, 1, 1};
  int k = solution.removeElement(nums, 1);
  EXPECT_EQ(k, 0);
}

TEST(RemoveElementTest, NoneMatch) {
  Solution solution;
  std::vector<int> nums = {1, 2, 3};
  int k = solution.removeElement(nums, 4);
  EXPECT_EQ(k, 3);
  std::sort(nums.begin(), nums.begin() + k);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{1, 2, 3}));
}

TEST(RemoveElementTest, EmptyArray) {
  Solution solution;
  std::vector<int> nums = {};
  int k = solution.removeElement(nums, 1);
  EXPECT_EQ(k, 0);
}

TEST(RemoveElementTest, SingleElementMatch) {
  Solution solution;
  std::vector<int> nums = {5};
  int k = solution.removeElement(nums, 5);
  EXPECT_EQ(k, 0);
}

TEST(RemoveElementTest, SingleElementNoMatch) {
  Solution solution;
  std::vector<int> nums = {5};
  int k = solution.removeElement(nums, 3);
  EXPECT_EQ(k, 1);
  EXPECT_EQ(nums[0], 5);
}

TEST(RemoveElementTest, ValAtEnds) {
  Solution solution;
  std::vector<int> nums = {7, 1, 2, 3, 7};
  int k = solution.removeElement(nums, 7);
  EXPECT_EQ(k, 3);
  std::sort(nums.begin(), nums.begin() + k);
  EXPECT_EQ((std::vector<int>{nums.begin(), nums.begin() + k}),
            (std::vector<int>{1, 2, 3}));
}
