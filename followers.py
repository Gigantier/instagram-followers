import sys
import os
import instaloader

# Get instance
L = instaloader.Instaloader()
L.login(os.getenv('INSTAGRAM_USER'), os.getenv('INSTAGRAM_PASSWORD'))

profile = instaloader.Profile.from_username(L.context, sys.argv[1])

# Print list of followees
for person in profile.get_followers():
  print (person.username)