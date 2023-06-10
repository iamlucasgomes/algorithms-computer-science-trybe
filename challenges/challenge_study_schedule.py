def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    students = 0
    for start_period, end_period in permanence_period:
        if not isinstance(start_period, int) or not isinstance(
            end_period, int
        ):
            return None
        if start_period <= target_time <= end_period:
            students += 1
    return students
