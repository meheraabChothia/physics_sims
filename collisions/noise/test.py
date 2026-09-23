import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise1 = PerlinNoise(n_dims=2, octaves=0.5)
noise2 = PerlinNoise(n_dims=2, octaves=1)
noise3 = PerlinNoise(n_dims=2, octaves=2)
noise4 = PerlinNoise(n_dims=2, octaves=4)

xpix = 100
ypix = 100
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='gray')
plt.show()
