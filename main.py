from crew import TravelingCrew

if __name__ == '__main__':
    city = "Gdansk"  #miasto
    inputs = {
        "city": city,
    }
    TravelingCrew().crew().kickoff(inputs=inputs)
