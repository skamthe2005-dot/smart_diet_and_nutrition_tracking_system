
def daily_requirement(profile):
    age=profile.age
    height=profile.height
    weight=profile.weight
    activity=profile.activity_level
    gender=profile.gender
    goal=profile.fitness_goal

    if gender=="male":
        bmr=(10*weight)+(6.2*height)-(5*age)+5

    elif gender=="female":
        bmr=(10*weight)+(6.2*height)-(5*age)+161

    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 78

    activity_factor={
        "sedentary":1.2,
        "light":1.375,
        "moderate":1.55,
        "active":1.275
    }

    activity_factor=activity_factor[activity]

    tdee=bmr*activity_factor

    if goal=="weight gain":
        calories_target=tdee+300

    elif goal=="weight loss":
        calories_target=tdee-300

    else:
        calories_target=tdee

    if goal == "maintenance":
        protein_factor = 1.2
    else:
        protein_factor = 1.6

    protein_target = weight * protein_factor

    # Return calculated values
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "calories_target": round(calories_target),
        "protein_target": round(protein_target)
    }

