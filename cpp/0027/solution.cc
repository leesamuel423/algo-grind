#include "solution.h"

int Solution::removeElement(std::vector<int> &nums, int val) {
  int n = nums.size();
  for (int i = 0; i < n;) {
    if (nums[i] == val)
      nums[i] = nums[--n];
    else
      i++;
  }
  return n;
}
