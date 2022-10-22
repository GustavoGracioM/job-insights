from .jobs import read


def get_unique_job_types(path: str):
    jobs = read(path)
    job_type = set()
    for job in jobs:
        job_type.add(job["job_type"])

    return job_type


def filter_by_job_type(jobs: dict, job_type: str):
    return [job for job in jobs if job_type == job["job_type"]]


def get_unique_industries(path):
    resul = read(path)
    industry = set()
    jobs = [job for job in resul if "industry" in job]
    for job in jobs:
        if len(job["industry"]) != 0:
            industry.add(job["industry"])

    return industry


def filter_by_industry(jobs, industry):
    return [
        job for job in jobs if "industry" in job if industry == job["industry"]
    ]


def get_max_salary(path):
    resul = read(path)
    jobs = [
        int(job["max_salary"])
        for job in resul
        if "max_salary" in job
        if job["max_salary"].isdigit()
    ]
    return max(jobs)


def get_min_salary(path):
    resul = read(path)
    jobs = [
        int(job["min_salary"])
        for job in resul
        if "min_salary" in job
        if job["min_salary"].isdigit()
    ]
    return min(jobs)


def matches_salary_range(job: dict, salary: int):
    if not (
        "max_salary" in job and "min_salary" in job and isinstance(salary, int)
    ):
        raise ValueError("min_salary or max_salary are not present in job")
    if not (
        isinstance(job["max_salary"], int)
        or isinstance(job["min_salary"], int)
    ):
        raise ValueError("min_salary or max_salary is not number")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("error")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
