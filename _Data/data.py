from enum import Enum

class HomePageData:
    LIST_YOUR_PROPERTIES_PAGE_TITLE = "Goibibo & MakeMytrip - Free Hotel Registration - Add your Hotel with Connect (Ingo-MMT)"

    NAVIGATION_BAR_ELEMENTS = [
        "Flights", "Hotels", "Homestays & Villas", "Holiday Packages",
        "Trains", "Buses", "Cabs", "Forex Card & Currency", "Travel Insurance"
    ]

    DOMESTIC_CITIES = [
        "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai",
        "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
    ]

    INTERNATIONAL_CITIES = [
        "Dubai", "Singapore", "London", "New York", "Paris",
        "Bangkok", "Sydney", "Toronto", "Kuala Lumpur", "Tokyo"
    ]

    TRAVEL_DATE = "apr 28, 2025"

class TripType(Enum):
    ONE_WAY = "One Way"
    ROUND_TRIP = "Round Trip"
    MULTI_CITY = "Multi City"

class FareType(Enum):
    REGULAR = "Regular"
    STUDENT = "Student"
    SENIOR_CITIZEN = "Senior Citizen"
    ARMED_FORCES = "Armed Forces"
    DOCTOR_NURSE = "Doctor and Nurse"

class FlightPageData:
    TRIP_TYPES = [trip.value for trip in TripType]
    FARE_TYPES = [fare.value for fare in FareType]

    @staticmethod
    def get_city(index, cities_list):
        return cities_list[index] if index < len(cities_list) else "Unknown"

    FILTERS = [
        "Applied Filters",
        "Popular Filters",
        "One Way Price",
        f"Stops From {HomePageData.DOMESTIC_CITIES[1]}",
        f"Departure From {HomePageData.DOMESTIC_CITIES[1]}",
        f"Arrival at {HomePageData.INTERNATIONAL_CITIES[1]}",
        "Airlines"
    ]
    