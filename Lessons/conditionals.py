"""Practicing conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10"""
    if num < 10:
        print("small number")  # then block
    else:
        print("big number")
    print("this is the end of the function")


(less_than_10(num=2))

def wake_up(alarm:bool) -> str:
"""returns a message based on if an alarm is going off"""
    if alarm is True:
        return "wake up"
    else:
        return "Keep sleeping"
    print(wake_up(alarm=True))

def check_first_letter(word:str,letter:str) -> str:
    if word[0] == letter:
        return"match"
    else:
        return "no match"
    
print(check_first_letter(word="happy",letter="s"))




def get_weather_report() -> str:
    weather: str = input("what is the weather?")
    if weather == "rainy" or weather =="cold"
        print("bring a jacket")
    elif weather == "hot"
        print("keep cool")
    else:
        print("")
    return weather



