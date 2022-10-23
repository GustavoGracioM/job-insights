from src.sorting import sort_by

mock = [
    {
        "min_salary": "3",
        "max_salary": "10",
        "date_posted": "2020-05-01",
    },
    {
        "min_salary": "1",
        "max_salary": "2",
        "date_posted": "2020-05-07",
    },
]

order_min = [
    {
        "min_salary": "1",
        "max_salary": "2",
        "date_posted": "2020-05-07",
    },
    {
        "min_salary": "3",
        "max_salary": "10",
        "date_posted": "2020-05-01",
    },
]

order_max = [
    {
        "min_salary": "3",
        "max_salary": "10",
        "date_posted": "2020-05-01",
    },
    {
        "min_salary": "1",
        "max_salary": "2",
        "date_posted": "2020-05-07",
    },
]

order_data_posted = [
    {
        "min_salary": "1",
        "max_salary": "2",
        "date_posted": "2020-05-07",
    },
    {
        "min_salary": "3",
        "max_salary": "10",
        "date_posted": "2020-05-01",
    },
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == order_min
    sort_by(mock, "max_salary")
    assert mock == order_max
    sort_by(mock, "date_posted")
    assert mock == order_data_posted
