import matplotlib.pyplot as plt
import numpy as np
# 1)

# def f(x):
#   return x**2

# xverdier = np.linspace(0, 10, 101)
# yverdier = f(xverdier)

# plt.plot(xverdier, yverdier)
# plt.show()

# 3)
# x= []
# y = []

# def f(x):
#     return 2*x - 3

# for i in range(11):
#     x.append(i)
#     y.append(f(i))

# #plt.plot(x, y, color="coral", linestyle="dotted")
# #plt.grid()
# #plt.title("$f(x)=2x-3$")
# plt.style.use("bmh")
# plt.plot(x, y)
# plt.xlabel("$x$")
# plt.ylabel("$y$")

# plt.show()


# 4)
# xverdier = np.linspace(0, 20, 50)

# # Graf 1
# yverdier = 2*xverdier + 1

# plt.subplot(2, 2, 1)
# plt.plot(xverdier, yverdier)
# plt.grid()

# # Graf 2
# yverdier = xverdier**2 - 3

# plt.subplot(2, 2, 2)
# plt.plot(xverdier, yverdier)
# plt.grid()

# # Graf 3
# yverdier = 2**xverdier 

# plt.subplot(2, 2, 3)
# plt.plot(xverdier, yverdier)
# plt.grid()

# # Graf 4
# yverdier = xverdier/3

# plt.subplot(2, 2, 4)
# plt.plot(xverdier, yverdier)
# plt.grid()

# plt.show()

# 6)
