#include <gtest/gtest.h>
#include "cpp/0217/solution.h"

TEST(ContainsDuplicateTest, HasDuplicates) {
    Solution solution;
    const std::vector<int> nums = {1, 2, 3, 1};
    EXPECT_TRUE(solution.containsDuplicate(nums));
}

TEST(ContainsDuplicateTest, NoDuplicates) {
    Solution solution;
    const std::vector<int> nums = {1, 2, 3, 4};
    EXPECT_FALSE(solution.containsDuplicate(nums));
}

TEST(ContainsDuplicateTest, MultipleDuplicates) {
    Solution solution;
    const std::vector<int> nums = {1, 2, 2, 3, 3, 4, 3, 2, 4, 2};
    EXPECT_TRUE(solution.containsDuplicate(nums));
}
