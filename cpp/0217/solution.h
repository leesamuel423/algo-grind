#ifndef SOLUTION_H
#define SOLUTION_H

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool containsDuplicate(const std::vector<int>& nums) {
        std::unordered_set<int> set(nums.begin(), nums.end());
        return set.size() != nums.size();
    }
};

#endif // SOLUTION_H
