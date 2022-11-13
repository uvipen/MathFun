"""
@author: Viet Nguyen <nhviet1009@gmail.com>
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Uncomment the 2 lines below to have a better output resolution
#plt.rcParams['figure.dpi'] = 300
#plt.rcParams['savefig.dpi'] = 300

static_frames = 100
num_samples = 100

fig = plt.figure()
ax = fig.add_subplot(xlim=(-2, 2), ylim=(-2, 2))
ax.set_yticklabels([])
ax.set_xticklabels([])

# Draw head
theta = np.linspace(0, 2 * np.pi, num_samples)
a = 0.3 * np.cos(theta)
b = 0.3 + 0.3 * np.sin(theta)
ax.plot(a, b, "#1f77b4")

# Draw eyes
theta = np.linspace(-np.pi, np.pi, num_samples)
a = 0.03 * np.cos(theta) - 0.1
b = 0.4 + 0.05 * np.sin(theta)
ax.plot(a, b, "#1f77b4")
a = 0.03 * np.cos(theta) + 0.1
b = 0.4 + 0.05 * np.sin(theta)
ax.plot(a, b, "#1f77b4")

# Draw mouth
gamma = np.linspace(-np.pi, 0, num_samples)
a = 0.15 * np.cos(gamma)
b = 0.2 + 0.08 * np.sin(gamma)
ax.plot(a, b, "#1f77b4")

# Draw body
a = 0.3 * np.cos(theta)
b = -0.5 + 0.5 * np.sin(theta)
ax.plot(a, b, "#1f77b4")
ax.scatter(0, -0.5, s=640, marker='*', color='gold', zorder=3)

# Draw legs
a = np.linspace(-0.1, -0.23, num_samples)
b = 7 * a - 0.28
ax.plot(a, b, "#1f77b4")
a = np.linspace(0.1, 0.23, num_samples)
ax.plot(a, b, "#1f77b4")

# Draw foot
a = 0.1 * np.cos(theta) - 0.3
b = -1.95 + 0.05 * np.sin(theta)
ax.plot(a, b, "#1f77b4")
a = 0.1 * np.cos(theta) + 0.3
b = -1.95 + 0.05 * np.sin(theta)
ax.plot(a, b, "#1f77b4")

ax.set_aspect('equal')
ax.grid()
shift = 0.1
x = np.concatenate([np.linspace(shift, 1, num_samples), np.ones(static_frames)])

x_right = np.empty(0)
y_right = np.empty(0)
x_left = np.empty(0)
y_left = np.empty(0)
z = []
alignment = []

# y=x
y = x - shift
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["x" for _ in range(num_samples + static_frames)])
alignment.extend([0.3 for _ in range(num_samples + static_frames)])

# y = -x
y = -x + shift
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["-x" for _ in range(num_samples + static_frames)])
alignment.extend([0.27 for _ in range(num_samples + static_frames)])

# y=|x|
y = np.abs(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["|x|" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=-|x|
y = -np.abs(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["-|x|" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=x^2
y = (x - shift) ** 2
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend([r"$x^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=-x^2
y = -(x - shift) ** 2
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend([r"$-x^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.21 for _ in range(num_samples + static_frames)])

# y=x^3
y = (x - shift) ** 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend([r"$x^3$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=sin x
y = np.sin(3.05 * (x - shift)) / 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["sin x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=cos x
y = np.cos(3.05 * (x - shift)) / 3 - 1 / 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["cos x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=tan x
y = np.tan(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["tan x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=cot x
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, -y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["cot x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=e^x
x_e = np.concatenate([np.linspace(shift, 1.2, num_samples), np.ones(static_frames)])
y = np.power(np.e, x_e/2)-1-shift/2
x_right = np.concatenate([x_right, x_e])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x_e])
y_left = np.concatenate([y_left, np.power(np.e, -x_e/2)-1+shift/2])
z.extend([r"$e^x$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# x^2+y^2=R^2
y_2 = np.concatenate([np.linspace(0, 1, num_samples), np.ones(static_frames)])
x_2 = np.sqrt(0.25-(y_2-0.5)**2)
x_right = np.concatenate([x_right, x_2])
y_right = np.concatenate([y_right, y_2])
x_left = np.concatenate([x_left, -x_2])
y_left = np.concatenate([y_left, y_2])
z.extend([r"$x^2+y^2=R^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.05 for _ in range(num_samples + static_frames)])

length = len(x_right)
line1, = ax.plot(np.empty(length), np.empty(length), "r", lw=2)
line2, = ax.plot(np.empty(length), np.empty(length), "r", lw=2)
display_template = 'y = %s'
display_text = ax.text(0.3, 0.85, '', transform=ax.transAxes, fontsize=40, color="m")


def animate(i):
    first_idx = i // (num_samples + static_frames) * (num_samples + static_frames)
    line1.set_data(x_right[first_idx:i], y_right[first_idx:i])
    line2.set_data(x_left[first_idx:i], y_left[first_idx:i])
    if z[i] != r"$x^2+y^2=R^2$":
        display_text.set_text(display_template % z[i])
    else:
        display_text.set_text(z[i])
    display_text.set_x(alignment[i])
    return line1, line2, display_text


ani = animation.FuncAnimation(fig, animate, np.arange(length),
                              interval=10, blit=True, repeat=False)
ani.save('MathFun.mp4', fps=60)
plt.show()
