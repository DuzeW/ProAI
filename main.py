from crew import TravelingCrew

if __name__ == '__main__':
    city = "Warsaw" #miasto
    preferred_weather = "sunny" #Opcje deszcz słonecznie pochmurnie śnieg
    answer_language = "Polish"#Opcje Polski angielski japoński(dla preferencji ćwiczeniowca) front dajnie jak by też się zmieniał
    budget = "middle"#High middle low
    preferred_transportation = "private" #Opcje Public Private
    point_of_interest = "business" #Niech sam sobie wpisze
    preferred_accommodation = ""
    inputs = {
        "city": city,
        "preferred_weather": preferred_weather,
        "answer_language": answer_language,
        "budget": budget,
        "preferred_transportation": preferred_transportation,
        "point_of_interest": point_of_interest,
        "preferred_accommodation": preferred_weather,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)