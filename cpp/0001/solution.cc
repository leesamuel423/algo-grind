#include "solution.h"

#include <map>

std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
  std::map<int, int> cache;

  for (int i = 0; i < nums.size(); i++) {
    const int remainder = target - nums[i];
    if (cache.find(remainder) != cache.end()) {
      return {cache[remainder], i};
    } else {
      cache[nums[i]] = i;
    }
  }

  return {-1};
}
