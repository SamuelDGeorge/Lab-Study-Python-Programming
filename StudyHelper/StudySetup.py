import StudyHelper.OnlineLogger as OnlineLogger

def StudySetup(unique_id, course_taken, notebook_name, ident):
    base_id = unique_id + '-' + course_taken + '-'
    OnlineLogger.start(notebook_name, ident, base_id)
    print("Ready to begin study!")