class PageInfo:
    url = 'https://staging.karirlab.co/dashboard/resume-review-submission'
    title = "#resumeEvaluationTitle"
    description = "#resumeEvaluationDescription"
    standard_item = "#resumeEvaluationFeatureStandarCard"
    evaluation_item = "#resumeEvaluationFeatureEvaluationCard"

class Action:
    back_action = "#backResumeEvaluation"
    title = "//h1[contains(@class, 'resumeReviewSubmission__title')]"
    upload_area = "//input[@id='uploadResumeDragger']"
    btn_choose = "#selectResumeButton"
    btn_upload = "#uploadResumeButton"
    select_industry = "//input[@id='industrySelect']"
    list_industry = "#industrySelectList"
    select_jobFunction = "//input[@id='jobFunctionSelect']"
    list_ijobFunction = "#jobFunctionSelectList"
    btn_submit = "#submitEvaluationButton"


# Copy dari resume builder aja?
# class Preview: