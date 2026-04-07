#include "cpp/0346/solution.h"
#include <gtest/gtest.h>

TEST(MovingAverageTest, Example1) {
  MovingAverage ma(3);
  EXPECT_DOUBLE_EQ(ma.next(1), 1.0);
  EXPECT_DOUBLE_EQ(ma.next(10), 5.5);
  EXPECT_NEAR(ma.next(3), 4.66667, 1e-4);
  EXPECT_DOUBLE_EQ(ma.next(5), 6.0);
}
