# a small change2
# Imports will be cleaner eventually...
from MontyCarlo import *
from MontyCarlo.sources import *
from MontyCarlo.geometry.CSG import *


gold = Mat({79:1}, 1.93200000E+01, name = "Gold")



with InfiniteVolume() as outer:
    outer.configure("OUTER", render = False)
    outer.fill(gold) 
    
    with Z_TALLY(DZ = .01, zmax = 300) as tally:
        tally in outer
        tally.configure("outer_sphere", render = False)  ### <--- in the after_simulation branch the user has turned off render, so that it is read from cache
        tally.fill(gold)


photon_beam = Beam(
                   "electron",       # kind of particle 
                   tally,   # initial volume
                   E = 50e6,       # initial eneryg in eV
                   N = 1_00,     # number of particles in the source, careful with this number, might break your run and fill your ram
                   pos = (0, 0, 10) # initial position 
                  ) 



# let Plotter handle the run
plotter = Plotter(photon_beam)


# then ask it for a fig
fig = plotter.new_plot()

# use this method to draw the geometry onto the figure (this will be better)
#plotter.add_geometry(fig, outer)


fig.show()





for _ in range(10):
    photon_beam = Beam(
                       "electron",       # kind of particle 
                       tally,   # initial volume
                       E = 50e6,       # initial eneryg in eV
                       N = 1_000,     # number of particles in the source, careful with this number, might break your run and fill your ram
                       pos = (0, 0, 10) # initial position 
                      ) 


    photon_beam.run()

    x, y = tally.get_bins()

    plt.plot(x, y/max(y))

plt.show()
