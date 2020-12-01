"""

  if statements
  
"""

def home(bedroom = 8, parlour = "8", duplex = True ):
  if bedroom == int(parlour):
    duplex = True
  else:
    duplex =False
  print(duplex)
home()