import StudyHelper.OnlineLogger as OnlineLogger


def StudySetup(unique_id, course_taken, notebook_name, ident):
    if unique_id == "FakeName123":
        print("Please edit the 'chosen_id' above to a new fake name.")
        return
    base_id = unique_id + "-" + course_taken + "-"
    OnlineLogger.start(notebook_name, ident, base_id)
    print("Ready to begin study!")
