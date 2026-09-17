import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "src")
)

from attendance_advisor import (
    calculate_attendance,
    get_recommendation
)


def test_attendance_percentage():
    result = calculate_attendance(32, 40)

    assert result == 80.0


def test_zero_classes():
    result = calculate_attendance(0, 0)

    assert result == 0


def test_full_attendance():
    result = calculate_attendance(40, 40)

    assert result == 100.0


def test_half_attendance():
    result = calculate_attendance(20, 40)

    assert result == 50.0


def test_maximum_safe_skips():
    status, result = get_recommendation(
        32, 40, 75
    )

    assert status == "COMPLIANT"
    assert result == 2


def test_below_goal():
    status, result = get_recommendation(
        25, 40, 75
    )

    assert status == "BELOW_GOAL"
    assert result == 20


def test_exact_threshold():
    status, result = get_recommendation(
        30, 40, 75
    )

    assert status == "COMPLIANT"
    assert result == 0


def test_no_classes():
    status, result = get_recommendation(
        0, 0, 75
    )

    assert status == "NO_DATA"


def test_invalid_attendance():
    status, result = get_recommendation(
        45, 40, 75
    )

    assert status == "ERROR"