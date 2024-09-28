#include <gtest/gtest.h>
#include "cpp/0155/solution.h"

TEST(MinStackTest, Test1) {
  std::vector<std::string> operations = {"MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"};
  std::vector<std::vector<int>> arguments = {{}, {-2}, {0}, {-3}, {}, {}, {}, {}};
  std::vector<int> expected = {0, 0, 0, 0, -3, 0, 0, -2};
  std::vector<int> actual;
  MinStack s;

  for (size_t i = 0; i < operations.size(); i++) {
    if (operations[i] == "MinStack") {
      continue;  // Constructor is already invoked
    } else if (operations[i] == "push") {
      s.push(arguments[i][0]);
    } else if (operations[i] == "pop") {
      s.pop();
    } else if (operations[i] == "top") {
      actual.push_back(s.top());
    } else if (operations[i] == "getMin") {
      actual.push_back(s.getMin());
    }
  }

  std::vector<int> expectedNonNull = {-3, 0, -2};
  EXPECT_EQ(actual, expectedNonNull);
}
