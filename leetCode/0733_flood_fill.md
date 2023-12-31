# 733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

```
Example 1:
![Alt text](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
```

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

## JavaScript Solution

```js
const floodFill = function (image, sr, sc, color, firstColor = image[sr][sc]) {
  if (
    sr < 0 ||
    sc < 0 ||
    sr >= image.length ||
    sc > image[0].length ||
    image[sr][sc] !== firstColor ||
    image[sr][sc] === color
  )
    return image;

  image[sr][sc] = color;

  floodFill(image, sr + 1, sc, color, firstColor);
  floodFill(image, sr - 1, sc, color, firstColor);
  floodFill(image, sr, sc + 1, color, firstColor);
  floodFill(image, sr, sc - 1, color, firstColor);

  return image;
};
```

## Python Solution

```py
class Solution:
    def floodFill(self, image, sr, sc, color):
        starting = image[sr][sc]

        def recurse(image, sr, sc, color, starting):
            if (
                sr < 0
                or sc < 0
                or sr >= len(image)
                or sc >= len(image[sr])
                or image[sr][sc] != starting
                or image[sr][sc] == color
            ):
                return image

            image[sr][sc] = color
            print(image)
            recurse(image, sr + 1, sc, color, starting)
            recurse(image, sr - 1, sc, color, starting)
            recurse(image, sr, sc + 1, color, starting)
            recurse(image, sr, sc - 1, color, starting)

            return image

        return recurse(image, sr, sc, color, starting)
```

- Time Complexity: O(m \* n)
- Space Complexity: O(m \* n)

- Recursive solution
- Base case is if the current pixel is not the same color as the starting pixel or if the current pixel is already the new color or if the current pixel is out of bounds
- Otherwise, change the current pixel to the new color and recursively call floodFill on the 4-directionally adjacent pixels
