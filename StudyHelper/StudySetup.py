import StudyHelper.OnlineLogger as OnlineLogger

def StudySetup(unique_id, course_taken):
    notebook_name = "Study_Notebook.ipynb"
    unique_logset_identifier = "Lab_Study_Comp116_A3_Q2_Spring_2023"
    base_id = unique_id + '-' + course_taken + '-'
    OnlineLogger.start(notebook_name, unique_logset_identifier, base_id)
    print("Ready to begin study!")