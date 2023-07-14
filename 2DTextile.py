# 2DTextile.py

# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *

# Specify weave parameters
nwarp=2   #Number of weft yarns in the unit cell
nweft=2    #Number of warp yarns in the unit cell
s=1          #Spacing between the yarns
t=0.1       #Thickness of the fabric (sum of two yarn heights)
ref=True  #Refine model (True/False)

# Create 2D textile
weave = CTextileWeave2D( nweft, nwarp, s, t, ref )

# Set the weave pattern
weave.SwapPosition(0, 0)
weave.SwapPosition(1, 1)

#Add to the textile database
AddTextile(weave)
