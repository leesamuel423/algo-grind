#include "solution.h"

MovingAverage::MovingAverage(int size) { v.resize(size, 0); }

double MovingAverage::next(int val) {
  if (count < (int)v.size()) {
    count += 1;
  }
  sum += val - v[idx];
  v[idx] = val;
  idx = (idx + 1) % v.size();
  return sum / count;
}
