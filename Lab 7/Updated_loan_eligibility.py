CATEGORIES = {
    "P": "Individual",
    "C": "Company",
    "H": "HUF",
    "F": "Firm"
}


def parse_income(income):
    try:
        if income is None:
            return None

        return int(income.replace(',', ''))
    except (ValueError, AttributeError):
        return None


def monthly_emi(details):
    try:
        if details is None:
            return None

        principal, rate, years = details.split(',')

        principal = int(principal)
        rate = float(rate)
        years = int(years)

        if principal <= 0 or rate < 0 or years <= 0:
            return None

        r = rate / 1200
        n = years * 12

        if r == 0:
            return round(principal / n, 2)

        return round(
            principal * r * (1 + r) ** n /
            ((1 + r) ** n - 1), 2
        )

    except (ValueError, AttributeError, ZeroDivisionError):
        return None


def pan_category(pan):
    try:
        if pan is None or len(pan) < 4:
            return None

        return CATEGORIES.get(pan[3].upper())

    except (TypeError, AttributeError):
        return None


def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    result = parse_income(user_input)
    print("Income:", result)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    result = monthly_emi(user_input)
    print("Monthly EMI:", result)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    result = pan_category(user_input)
    print("PAN Category:", result)


if __name__ == "__main__":
    main()