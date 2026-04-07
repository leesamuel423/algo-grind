#include "cpp/0088/solution.h"
#include <gtest/gtest.h>

TEST(MergeTest, BasicMerge) {
  Solution solution;
  std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
  std::vector<int> nums2 = {2, 5, 6};
  solution.merge(nums1, 3, nums2, 3);
  EXPECT_EQ(nums1, (std::vector<int>{1, 2, 2, 3, 5, 6}));
}

TEST(MergeTest, Nums2Empty) {
  Solution solution;
  std::vector<int> nums1 = {1};
  std::vector<int> nums2 = {};
  solution.merge(nums1, 1, nums2, 0);
  EXPECT_EQ(nums1, (std::vector<int>{1}));
}

TEST(MergeTest, Nums1Empty) {
  Solution solution;
  std::vector<int> nums1 = {0};
  std::vector<int> nums2 = {1};
  solution.merge(nums1, 0, nums2, 1);
  EXPECT_EQ(nums1, (std::vector<int>{1}));
}

TEST(MergeTest, Nums2AllSmaller) {
  Solution solution;
  std::vector<int> nums1 = {4, 5, 6, 0, 0, 0};
  std::vector<int> nums2 = {1, 2, 3};
  solution.merge(nums1, 3, nums2, 3);
  EXPECT_EQ(nums1, (std::vector<int>{1, 2, 3, 4, 5, 6}));
}

TEST(MergeTest, Nums2AllLarger) {
  Solution solution;
  std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
  std::vector<int> nums2 = {4, 5, 6};
  solution.merge(nums1, 3, nums2, 3);
  EXPECT_EQ(nums1, (std::vector<int>{1, 2, 3, 4, 5, 6}));
}

TEST(MergeTest, Duplicates) {
  Solution solution;
  std::vector<int> nums1 = {1, 1, 1, 0, 0, 0};
  std::vector<int> nums2 = {1, 1, 1};
  solution.merge(nums1, 3, nums2, 3);
  EXPECT_EQ(nums1, (std::vector<int>{1, 1, 1, 1, 1, 1}));
}

TEST(MergeTest, NegativeNumbers) {
  Solution solution;
  std::vector<int> nums1 = {-3, -1, 0, 0, 0};
  std::vector<int> nums2 = {-2, 4, 5};
  solution.merge(nums1, 2, nums2, 3);
  EXPECT_EQ(nums1, (std::vector<int>{-3, -2, -1, 4, 5}));
}
