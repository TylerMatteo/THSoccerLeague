import csv

if __name__ == "__main__":
	inexperienced = []
	experienced = []

	# Seperate players into two groups based on experience
	with open('players.csv') as file:
		reader = csv.DictReader(file, delimiter=',')
		for row in reader:
			if row["Soccer Experience"] == "YES":
				experienced.append(row)
			else:
				inexperienced.append(row)

	# Build teams, each with a third of the experienced players and a third of the inexperienced players
	dragons = dict.fromkeys(['players', 'practice', 'name'])
	sharks = dict.fromkeys(['players', 'practice', 'name'])
	raptors = dict.fromkeys(['players', 'practice', 'name'])

	dragons["players"]= experienced[:3] + inexperienced[:3] 
	sharks["players"] = experienced[3:6] + inexperienced[3:6] 
	raptors["players"] = experienced[6:9] + inexperienced[6:9] 

	#Assign practice dates and names to each team object
	dragons["practice"] = "March 17, 1pm"
	dragons["name"] = "Dragons"
	sharks["practice"] = "March 17, 3pm"
	sharks["name"] = "Sharks"
	raptors["practice"] = "March 18, 1pm"
	raptors["name"] = "Raptors"

	# Build function to write letters for each team
	def WriteLettersForTeam(team):
		for player in team["players"]:
			message = """Dear {},

			{} has been placed on the {} team.
			Their first practice time is {}


			Good luck!""".format(player["Guardian Name(s)"], player["Name"], team["name"], team["practice"])


			file = open(player["Name"]+".txt", "w")
			file.write(message)
			file.close


	# Call that function for each team
	WriteLettersForTeam(dragons)
	WriteLettersForTeam(sharks)
	WriteLettersForTeam(raptors)




