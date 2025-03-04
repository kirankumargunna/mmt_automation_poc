from datetime import datetime
from dateutil.relativedelta import relativedelta



def verify_comparison(expected, actual, fail_message=None):
    """
    Uses verify to perform a straight comparison. Actual can take a function signature or string value.
    This function will also format the fail message.
    :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
    :param actual: If this is an instance method, pass this in as a signature (ie, no parenthesis).
    :param fail_message: Message to send to console on failure
    :return:
    # """
    # if inspect.ismethod(actual):
    #     verify(lambda: actual() == expected, fail_message=get_formatted_fail_message(expected, actual(), fail_message))
    # else:
    #     verify(lambda: actual == expected, fail_message=get_formatted_fail_message(expected, actual, fail_message))

def get_formatted_fail_message(expected,actual,error_message):
    if error_message is None:
        error_message="The actual value does not match the expected value."
    return "{0}\n Actual:'{1}'\n Expected:{2}".format(error_message,actual,expected)


def convert_date(date_input)-> tuple[str, str] | str:
    formats = [
        "%Y-%m-%d",        # 2024-11-30
        "%d/%m/%Y",        # 30/11/2024
        "%m-%d-%Y",        # 11-30-2024
        "%B %d, %Y",      # November 30, 2024
        "%b %d, %Y",      # Nov 30, 2024
        "%Y/%m/%d",       # 2024/11/30
        "%d %B %Y",       # 30 November 2024
        "%d %b %Y",       # 30 Nov 2024
        "%m/%d/%Y",       # 11/30/2024
        "%Y.%m.%d",       # 2024.11.30
        "%d-%m-%Y",       # 30-11-2024
        "%Y%m%d",         # 20241130
        "%A, %d %B %Y",   # Saturday, 30 November 2024
        "%a, %d %b %Y",   # Sat, 30 Nov 2024
        "%d %m %Y",       # 30 11 2024
        ]

    for fmt in formats:
        try:
            parsed_date=datetime.strptime(date_input,fmt)
            month_year = parsed_date.strftime("%B %Y")
            return parsed_date.strftime("%a %b %d %Y"), month_year

        except ValueError:
            continue
    return "invalid date format"



def is_valid_date(user_date)-> bool:
    """
    Check if the user-provided date is within the range of 3 months from today's date.
    """
    today = datetime.today()
    # three_months_later = today + timedelta(days=90)  # Approximate 3 months as 90 days
    three_months_later = today + relativedelta(months=3)


    # Check if the input date is within the range of today and 3 months from now
    if today <= user_date <= three_months_later:
        return True
    return False



def get_date_of_travel(date)-> tuple[str, str]:
    """
    Prompt the user to input a valid date within the next 3 months in various formats.
    """
    while True:
        
        converted_date, month_year = convert_date(date)

        if converted_date == "invalid date format":
            print("Invalid date format. Please try again.")
            continue

        # Convert string to datetime object for range check
        user_date = datetime.strptime(converted_date, "%a %b %d %Y")

        if is_valid_date(user_date):
            print(f"Valid date entered: {converted_date}")
            return converted_date, month_year
        else:
            print("The date is outside the allowed range (next 3 months). Please try again.")