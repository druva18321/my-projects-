responses = {
  "black hole":"black holes are regions so strong that even light cant escape,fascinating yet terrfying.",
  "warp drive":"Warp drive is theoretically possible using Alcubierre's equations. We just need exotic matter. Simple right?",
  "alien": "Statistically speaking, we can't be alone. The universe is too vast for that.",
  "mars": "Mars is humanity's next step. Red, cold, and waiting.",
  "universe": "13.8 billion years old and still expanding. We know almost nothing about it.",
  "warp": "Alcubierre's warp drive theory bends spacetime itself. The ship doesn't move — space does.",
  "star": "Stars are nuclear fusion reactors. Our sun fuses 600 million tons of hydrogen every second.",
  "galaxy": "There are 2 trillion galaxies in the observable universe. We've barely explored one.",
  "light year": "One light year is 9.46 trillion kilometres. The nearest star is 4.2 light years away.",
  "nasa": "NASA has been pushing human boundaries since 1958. Still the gold standard of space exploration.",
}
follow_ups = {
    "black hole": "What fascinates you more — how they form or what's inside them?",
    "warp drive": "Do you think we'll crack warp drive in our lifetime?",
    "alien": "Do you think alien life would be friendly or hostile?",
    "star": "Did you know our sun will become a red giant in 5 billion years?",
    "galaxy": "Do you think we'll ever explore beyond the Milky Way?",
    "mars": "Would you go to Mars if you had the chance?",
    "universe": "Do you think the universe is infinite or has an edge?",
    "light year": "If you could travel at light speed where would you go first?",
    "nasa": "Do you think private companies like SpaceX will beat NASA someday?",
}
print ("NOVA online ask me any thing about space and science:")
while True:
  user = input("you").lower()
  if user == "quit":
    print("NOVA shutting down: Universe runs without Us")
    break
  matched =False
  for key in responses:
    if key in user:
       print("Nova:",responses[key])
       if key in follow_ups:
         print("NOVA:",follow_ups[key])
       matched= True 
       break
  if not matched:
    print("NOVA: Intresting question... Iam still learning about that")
 


