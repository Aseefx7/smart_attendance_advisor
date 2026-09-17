def calculate_attendance(attended, conducted):
    if conducted == 0:
        return 0

    return (attended / conducted) * 100


def get_recommendation(attended, conducted, threshold):
    """
    Goal-directed reasoning:
    Goal = maintain attendance at or above the threshold.
    """

    # Invalid values
    if attended < 0 or conducted < 0:
        return "ERROR", "Attendance values cannot be negative."

    # Attended cannot exceed conducted
    if attended > conducted:
        return "ERROR", "Attended classes cannot be greater than conducted classes."

    # No classes conducted
    if conducted == 0:
        return "NO_DATA", "No classes have been conducted yet."

    attendance = calculate_attendance(attended, conducted)

    # Goal is already satisfied
    if attendance >= threshold:

        max_skips = int(
            (attended / (threshold / 100)) - conducted
        )

        return "COMPLIANT", max_skips

    # Goal is not satisfied
    required_classes = 0

    while (
        (attended + required_classes)
        / (conducted + required_classes)
        * 100
    ) < threshold:

        required_classes += 1

    return "BELOW_GOAL", required_classes


def attendance_advisor(subject, attended, conducted, threshold):

    print("\n--------------------------------------")
    print("Subject:", subject)

    status, result = get_recommendation(
        attended,
        conducted,
        threshold
    )

    if conducted == 0:
        print("Current Attendance: No data")

    else:
        attendance = calculate_attendance(
            attended,
            conducted
        )

        print(
            "Current Attendance:",
            round(attendance, 2),
            "%"
        )

    print("Required Attendance:", threshold, "%")

    if status == "ERROR":

        print("Status: Error")
        print("Recommendation:", result)

    elif status == "NO_DATA":

        print("Status: No classes conducted yet.")
        print("Recommendation:", result)

    elif status == "COMPLIANT":

        print("Status: Goal satisfied.")

        if result > 0:
            print(
                "Maximum classes you can skip:",
                result
            )

            print(
                "Recommendation: You can skip up to",
                result,
                "class(es) and remain compliant."
            )

        else:
            print(
                "Maximum classes you can skip: 0"
            )

            print(
                "Recommendation: Attend upcoming classes "
                "to maintain the required attendance."
            )

    elif status == "BELOW_GOAL":

        print("Status: Below attendance goal.")

        print(
            "Classes you must attend:",
            result
        )

        print(
            "Recommendation: Attend the next",
            result,
            "consecutive class(es) to reach",
            threshold,
            "%."
        )


def main():

    print("======================================")
    print("       SMART ATTENDANCE ADVISOR")
    print("======================================")
    print(
        "Goal: Maintain attendance above "
        "the required threshold"
    )
    print()

    try:

        threshold = float(
            input(
                "Enter required attendance percentage: "
            )
        )

        if threshold <= 0 or threshold > 100:
            print(
                "Error: Threshold must be between 1 and 100."
            )
            return

        number_of_subjects = int(
            input("Enter number of subjects: ")
        )

        if number_of_subjects <= 0:
            print(
                "Error: Number of subjects must be greater than 0."
            )
            return

        for i in range(number_of_subjects):

            print("\n--- Subject", i + 1, "---")

            subject = input(
                "Enter subject name: "
            )

            attended = int(
                input("Enter classes attended: ")
            )

            conducted = int(
                input("Enter classes conducted: ")
            )

            attendance_advisor(
                subject,
                attended,
                conducted,
                threshold
            )

    except ValueError:

        print(
            "Error: Please enter valid numbers."
        )


if __name__ == "__main__":
    main()