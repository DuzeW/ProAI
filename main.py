from crew import TravelingCrew

if __name__ == '__main__':
    city = "Gdansk"  #miasto
    # preferred_transportation = "Private" #Opcje Public Private
    preferred_accommodation = "Hotel"
    inputs = {
        "city": city,
        "preferred_accommodation": preferred_accommodation,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)
