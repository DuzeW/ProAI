from crew import TravelingCrew

if __name__ == '__main__':
    city = "Gdansk"  #miasto
    answer_language = "Polski"  #Opcje Polski angielski japoński(dla preferencji ćwiczeniowca) front dajnie jak by też się zmieniał
    # preferred_transportation = "Private" #Opcje Public Private
    # point_of_interest = "History" #Niech sam sobie wpisze
    preferred_accommodation = "Hotel"
    inputs = {
        "city": city,
        "answer_language": answer_language,
        "preferred_accommodation": preferred_accommodation,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)
