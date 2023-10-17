#Define the dervied class Batsman
class Batsman():
  def play(self):
      print("The batsman is batting .")


# Define the derived class Bowler
class Bowler():
  def play( self):
      print("The bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman = Batsman ()
bowler = Bowler ()

# call the play() method for each object
batsman.play()
bowler.play()