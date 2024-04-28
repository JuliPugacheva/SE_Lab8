with open("data.csv") as file:
    next(file)
    survival_rates = {}
    for line in file:
        data = line.strip().split(',')
        age_str = f"{data[6]}"
        if age_str.isdigit():
            age = float(age_str)
        else:
            age = 0
        embarked = f"{data[12]}"
        survived = int(data[1])
        if age < 30:
            if embarked in survival_rates:
                total, survivors = survival_rates[embarked]
                survival_rates[embarked] = (total + 1, survivors + survived)
            else:
                survival_rates[embarked] = (1, survived)
    for embarked, (total, survivors) in survival_rates.items():
        survival_rates[embarked] = survivors / total
    print(survival_rates)
