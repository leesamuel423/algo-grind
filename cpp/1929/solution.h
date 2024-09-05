#ifndef SOLUTION_H
#define SOLUTION_H

#include <iostream>
#include <vector>
#include <map>

class Solution {
public:
  std::vector<int> getConcatenation(std::vector<int>& nums) {
    std::vector<int> output(nums);
    output.insert(output.end(), nums.begin(), nums.end());
    return output;
  }
};


#endif // SOLUTION_H
