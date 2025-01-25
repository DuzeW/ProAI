from crew import TravelingCrew

if __name__ == '__main__':
    city = "Warsaw" #miasto
    preferred_weather = "snowy" #Opcje deszcz słonecznie pochmurnie śnieg
    language = "en"#Opcje Polski angielski japoński(dla preferencji ćwiczeniowca) front dajnie jak by też się zmieniał
    budget = "High"#High middle low
    transportation = "Private" #Opcje Public Private
    interest = "Business" #Niech sam sobie wpisze
    inputs = {
        "city": city,
        "preferred_weather": preferred_weather,
        "answer_language": language,
        "budget": budget,
        "preferred_transportation": transportation,
        "point_of_interest": interest,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)