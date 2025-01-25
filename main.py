from crew import TravelingCrew

if __name__ == '__main__':
    city = "Gdansk" #miasto
    answer_language = "Polish"#Opcje Polski angielski japoński(dla preferencji ćwiczeniowca) front dajnie jak by też się zmieniał
    budget = "High"#High middle low
    preferred_transportation = "Private" #Opcje Public Private
    point_of_interest = "History" #Niech sam sobie wpisze
    preferred_accommodation = "Hotel"
    inputs = {
        "city": city,
        "answer_language": answer_language,
        "budget": budget,
        "preferred_transportation": preferred_transportation,
        "point_of_interest": point_of_interest,
        "preferred_accommodation": preferred_accommodation,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)