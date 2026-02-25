#1. You have a list of superheroes representing the Justice League
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Intial Team:",justice_league)

#Tasks
#1.Calculate the number of members in the Justice League.
print("No. of members:",len(justice_league))

#2.Batman recruited Batgirl and Nightwing as new members.Add them to your list.
justice_league.extend(['Batgirl','Nightwing'])
print("New members added:",justice_league)

#3.Wonder Woman is now the leader of the Justice League.Move her to the beginning of the list.
justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))
print("New list:",justice_league)

#4.Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league.remove("Superman")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Superman")
print("New List:", justice_league)

#5.The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League Team:", justice_league)

# 6.Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Sorted Team:", justice_league)
print("New Leader:", justice_league[0])
