class PageInfo:
    url = 'https://staging.karirlab.co/dashboard/resume-review-report/[resume_report_id]'
    back_action = "//a[contains(@class, 'BackNavigation_breadcrumbs')]"
    title = "//h1[contains(@class, 'resumeReviewReportScreen__title')]"


class ResumeSummary:
    title_wrapper = "#reviewSummaryWrapper"
    title_name = "#reviewSummaryName"
    title_rate = "#reviewSummaryRate"
    description = "#reviewSummaryDescription"
    target_industry = "#reviewSummaryIndustry"
    target_jobFunction = "#reviewSummaryJobFunction"

class ResumeScores:
    title = "#reviewScoresTitle"
    rating = "#reviewScoresRating"
    score = "#reviewScoresScore"
    format_item = "#reviewScoresFormat"
    format_title = "#reviewScoresFormatTitle"
    format_score = "#reviewScoresFormatScore"
    selfInfo_item = "#reviewScoresSelfInfo"
    selfInfo_title = "#reviewScoresSelfInfoTitle"
    selfInfo_score = "#reviewScoresSelfInfoScore"
    education_item = "#reviewScoresEducation"
    education_title = "#reviewScoresEducationTitle"
    education_score = "#reviewScoresEducationScore"
    occupation_item = "#reviewScoresOccupation"
    occupation_title = "#reviewScoresOccupationTitle"
    occupation_score = "#reviewScoresOccupationScore"
    proficiency_item = "#reviewScoresProficiency"
    proficiency_title = "#reviewScoresProficiencyTitle"
    proficiency_score = "#reviewScoresProficiencyScore"
    additionalInfo_item = "#reviewScoresAdditionalInfo"
    additionalInfo_title = "#reviewScoresAdditionalInfoTitle"
    additionalInfo_score = "#reviewScoresAdditionalInfoScore"
    fullscreen = "#resumeReviewFullScreen"
    
class ResumeReport:
    title = "#reviewReportTitle"
    score = "#reviewReportScore"
    prev_btn = "#reviewReportPrevBtn"
    next_btn = "#reviewReportNextBtn"
    report_items = "//div[@class='report_items']"
    report_item_title = "//div[@class='report_items']//h1[@class='report-item__title']"
    report_item_rating = "//div[@class='report_items']//span[@class='report-item__rating']"
    report_item_description = "//div[@class='report_items']//span[@class='report-item__description']"
    report_item_recommendation_wrapper = "//div[@class='report_items']//div[@class='report-item__recommendation']"
    report_item_recommendation_toggle = "//div[@class='report_items']//div[@class='report-item__recommendation_toggle']"
    report_item_recommendation_description = "//div[@class='report_items']//div[@class='report-item__recommendation_description']"
    report_sub_items = "//div[@class='report_subItems']//div[contains(@class, 'report-item__sub-item')]"
    report_sub_item_title = "//div[@class='report_subItems']//h3[@class='report-item__sub-title']"
    report_sub_item_description = "//div[@class='report_subItems']//span[@class='report-item__sub-description']"
    report_sub_item_rating = "//div[@class='report_subItems']//span[@class='report-item__sub-rating']"
    report_sub_item_recommendation = "//div[@class='report_subItems']//div[@class='report-item__sub-recommendation']"
    report_sub_item_recommendation_toggle = "//div[@class='report_subItems']//div[@class='report-item__sub-recommendation_toggle']"
    report_sub_item_recommendation_description = "//div[@class='report_subItems']//div[@class='report-item__sub-recommendation_description']"

# class ResumeReportFormats:
    # title = ""
    # score = ""

# class ResumeReportSelfInfo:

# class ResumeReportEducation:

# class ResumeReportOccupation: 

# class ResumeReportProficiency:

# class ResumeReportAdditionalInfo: