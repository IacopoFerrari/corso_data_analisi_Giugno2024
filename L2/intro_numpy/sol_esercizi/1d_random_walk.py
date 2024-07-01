pos=0
walk=[pos]
nsteps=1000
for _ in np.arange(nsteps):
    if np.random.randint(0,2):
        pos += 1
    else:
        pos -= 1

    walk.append(pos)

plt.plot(walk[0:100])