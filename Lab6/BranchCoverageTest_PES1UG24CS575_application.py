import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


# Credit band tests
def test_excellent_band():
    assert credit_band(800) == "excellent"


def test_good_band():
    assert credit_band(700) == "good"


def test_fair_band():
    assert credit_band(600) == "fair"


def test_poor_band():
    assert credit_band(400) == "poor"


@pytest.mark.parametrize("score", [299, 901])
def test_invalid_credit_score(score):
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(score)


# Loan eligibility tests
def test_eligible():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_self_employed_eligible():
    assert is_eligible(35, 50000, "self_employed", 700) is True


def test_unknown_employment():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "unemployed", 800)


@pytest.mark.parametrize("age", [20, 61])
def test_ineligible_age(age):
    assert is_eligible(age, 50000, "salaried", 800) is False


def test_minimum_age_eligible():
    assert is_eligible(21, 25000, "salaried", 650) is True


def test_maximum_age_eligible():
    assert is_eligible(60, 25000, "salaried", 650) is True


def test_insufficient_salaried_income():
    assert is_eligible(30, 24999, "salaried", 800) is False


def test_insufficient_self_employed_income():
    assert is_eligible(30, 39999, "self_employed", 800) is False


def test_poor_credit_ineligible():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_invalid_score_in_eligibility():
    with pytest.raises(ValueError, match="invalid score"):
        is_eligible(30, 50000, "salaried", 299)


# Interest rate tests
def test_excellent_salaried_without_collateral():
    assert interest_rate(800, "salaried", False) == 8


def test_good_salaried_without_collateral():
    assert interest_rate(700, "salaried", False) == 10


def test_fair_salaried_without_collateral():
    assert interest_rate(600, "salaried", False) == 13


def test_poor_salaried_without_collateral():
    assert interest_rate(400, "salaried", False) == 13


def test_self_employed_rate_adjustment():
    assert interest_rate(800, "self_employed", False) == 9


def test_collateral_rate_adjustment():
    assert interest_rate(800, "salaried", True) == 6


def test_self_employed_with_collateral():
    assert interest_rate(700, "self_employed", True) == 9


def test_invalid_score_in_interest_rate():
    with pytest.raises(ValueError, match="invalid score"):
        interest_rate(901, "salaried", False)