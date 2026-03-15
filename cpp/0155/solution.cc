#include "solution.h"

#include <algorithm>

void MinStack::push(int val) {
  s1.push(val);
  if (s2.empty()) {
    s2.push(val);
  } else {
    s2.push(std::min(s2.top(), val));
  }
}
