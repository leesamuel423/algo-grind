#include "solution.h"

void Solution::merge(std::vector<int> &nums1, int m, std::vector<int> &nums2,
                     int n) {
  int s = m + n - 1;
  m = m - 1;
  n = n - 1;
  while (s >= 0) {
    int first_vector = (m >= 0) ? nums1[m] : INT_MIN;
    int second_vector = (n >= 0) ? nums2[n] : INT_MIN;
    if (second_vector >= first_vector) {
      nums1[s] = second_vector;
      n -= 1;
    } else if (second_vector <= first_vector) {
      nums1[s] = first_vector;
      m -= 1;
    }
    s -= 1;
  }
}
