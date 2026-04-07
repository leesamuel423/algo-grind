#include "solution.h"

int Solution::removeDuplicates(std::vector<int> &nums) {
  if (nums.empty())
    return 0;
  int k = 1;
  for (int i = 1; i < nums.size(); i++) {
    if (nums[i] != nums[k - 1]) {
      nums[k] = nums[i];
      k += 1;
    }
  }
  return k;
}
