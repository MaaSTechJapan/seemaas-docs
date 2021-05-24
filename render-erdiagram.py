#%%
from eralchemy import render_er

inputdir = './erds/'
outputdir = './images/'

inputfile = 'traiire.er'
outputfile = 'erd_traiire.png'

render_er(f"{inputdir}{inputfile}", f"{outputdir}{outputfile}")
# %%

# %%
