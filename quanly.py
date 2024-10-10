class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class SportMatch:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)
        print(f"Match {match.name} has been added.")

    def remove_match(self, match_id):
        for match in self.matches:
            if match.match_id == match_id:
                self.matches.remove(match)
                print(f"Match {match_id} has been removed.")
                return
        print(f"Match {match_id} not found.")

class Person(SportMatch):
    def __init__(self, name, age, gender):
        super().__init__(name)
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Player(Person):
    def __init__(self, name, age, gender, player_number, player_position):
        super().__init__(name, age, gender)
        self.player_number = player_number
        self.player_position = player_position

    def get_player_info(self):
        return f"{self.get_details()}, Player Number: {self.player_number}, Position: {self.player_position}"

class Coach(Person):
    def __init__(self, name, age, gender, coaching_experience, managed_team):
        super().__init__(name, age, gender)
        self.coaching_experience = coaching_experience
        self.managed_team = managed_team

    def get_coach_info(self):
        return f"{self.get_details()}, Experience: {self.coaching_experience} years, Managed Team: {self.managed_team}"

class Referee(Person):
    def __init__(self, name, age, gender, experience_years):
        super().__init__(name, age, gender)
        self.experience_years = experience_years

    def get_referee_info(self):
        return f"{self.get_details()}, Experience: {self.experience_years} years"

class Team(SportMatch):
    def __init__(self, team_name):
        super().__init__(team_name)
        self.persons = []

    def add_person(self, person):
        if person not in self.persons:
            self.persons.append(person)
            print(f"{person.name} has been added to {self.name}.")
        else:
            print(f"{person.name} already exists in the team.")

    def remove_person(self, person):
        if person in self.persons:
            self.persons.remove(person)
            print(f"{person.name} has been removed from {self.name}.")
        else:
            print(f"{person.name} does not exist in the team.")

class Match(SportMatch):
    def __init__(self, match_id, team1, team2, referee, match_date):
        super().__init__(f"Match {match_id}")
        self.team1 = team1
        self.team2 = team2
        self.referee = referee
        self.match_date = match_date
        self.result = None

    def schedule_match(self):
        return f"{self.name}: {self.team1.name} vs {self.team2.name} on {self.match_date}, Referee: {self.referee.name}"

    def record_result(self, team1_score, team2_score):
        self.result = (team1_score, team2_score)
        return f"Match result recorded: {self.team1.name} {team1_score} - {self.team2.name} {team2_score}"




