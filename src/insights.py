from .jobs import read


def get_unique_job_types(path: str):
    jobs = read(path)
    job_type = set()
    for job in jobs:
        job_type.add(job["job_type"])

    return job_type


def filter_by_job_type(jobs: dict, job_type: str):
    return [job for job in jobs if job_type == job['job_type']]


def get_unique_industries(path):
    resul = read(path)
    industry = set()
    jobs = [job for job in resul if "industry" in job]
    for job in jobs:
        if len(job["industry"]) != 0:
            industry.add(job["industry"])

    return industry


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    resul = read(path)
    jobs = [
        int(job['max_salary'])
        for job in resul
        if "max_salary" in job
        if job["max_salary"].isdigit()
    ]
    return max(jobs)


def get_min_salary(path):
    resul = read(path)
    jobs = [
        int(job['min_salary'])
        for job in resul
        if "min_salary" in job
        if job["min_salary"].isdigit()
    ]
    return min(jobs)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
