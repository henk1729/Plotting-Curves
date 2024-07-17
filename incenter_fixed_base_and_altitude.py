# import libraries
import matplotlib.pyplot as plt
import numpy as np

# declare constants
A = np.array([-1, 0])
B = np.array([1, 0])
altitude = 1
x_range = np.linspace(-5, 5, 1000)
y = altitude

# function to calculate incenter
def incenter(A, B, C):
  # a, b, c are lengths of sides BC, CA, AB respectively
  a = np.linalg.norm(B-C)
  b = np.linalg.norm(C-A)
  c = np.linalg.norm(A-B)
  # formula for incenter(Ix, Iy) of triangle ABC is
  # Ix = (a*Ax + b*Bx + c*Cx)/(a + b + c)
  # Iy = (a*Ay + b*By + c*Cy)/(a + b + c)
  return (a*A + b*B + c*C)/(a + b + c)

# collect incenter points
incenters = []
for x in x_range:
  C = np.array([x, y])
  I = incenter(A, B, C)
  incenters.append(I)
incenters = np.array(incenters)

# plot locus
plt.figure(figsize=(8, 4))
# incenter locus- I
plt.scatter(incenters[:, 0], incenters[:, 1], c="blue", s=1, label="Incenter locus")
# fixed points- A, B
plt.scatter([A[0], B[0]], [A[1], B[1]], c="red", label="Fixed base points")
# third vertex- C
plt.scatter(x_range, np.full_like(x_vals, y), c="green", s=1, label="Third vertex locus")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Locus of Incenter of a triangle with fixed base points and a fixed altitude")
plt.grid(True)
plt.axis("equal")
plt.show()
