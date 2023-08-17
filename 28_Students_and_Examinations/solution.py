import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross_merged_data = students.merge(subjects, how='cross')
    examinations = examinations.groupby(['student_id', 'subject_name'])['subject_name'].count().reset_index(name='attended_exams')
    right_merged_data = examinations.merge(
        cross_merged_data, how='right', on=['student_id', 'subject_name']
    ).fillna(0)
    return right_merged_data[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(['student_id', 'subject_name'])