#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>

class MovingAverage {
private:
  std::vector<int> v;
  int idx = 0;
  int count = 0;
  double sum = 0;

public:
  MovingAverage(int size);
  double next(int val);
};

#endif // SOLUTION_H
