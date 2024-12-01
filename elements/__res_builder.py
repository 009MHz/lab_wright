class PageInfo:
    title = "//h3[contains(@class, 'FormLayout')]"
    url = 'https://staging.karirlab.co/resume-builder'


class ResumeInfo:
    title = "#resInfoTitle"
    name_label = "#resInfoNameTitle"
    name_input = "#resInfoNameField"
    lang_label = "#resInfoLangTitle"
    lang_input = "[overlayid='resInfoLangLists']"
    lang_id = "#resInfoLangID"
    lang_en = "#resInfoLangEN"
    goal_label = "#resInfoGoalTitle"
    goal_desc = "#resInfoGoalDesc"
    goal_input = "#resInfoGoalField"
    goal_content_empty = "div[overlayid='resInfoGoalLists'] .ant-select-selection-placeholder"
    goal_content_selected = "div[overlayid='resInfoGoalLists'] .ant-select-selection-item"
    goal_lists = "#resInfoGoalLists"
    goal_items = "(//div[contains(@class,'GoalItem')])"
    import_btn = "#resInfoImportBtn"
    import_modal = "//div[contains(@class, 'importDataModal')]"

    class ImportModal:
        title = "div[id=':r0:'] h3[class='ant-typography']"
        desc = "div[class='ant-modal-body'] span[class='ant-typography']"
        close = "#importDataCloseBtn"
        my_profile = "#importDataMyProfileBtn"
        my_resume = "#importDataMyResumeBtn"
        main_form = "//div[contains(@class, 'importDataModalMain')]"

        class Profile:
            title = "#DataProfTitle"
            desc = "#DataProfInfo"
            back_chevron = "#DataProfLeftChevron"
            cancel = "#DataProfCancelBtn"
            save = "#DataProfSaveBtn"

        class Resume:
            title = "#DataResTitle"
            desc = "#DataResInfo"
            back_chevron = "#DataResLeftChevron"
            cancel = "#DataResCancelBtn"
            save = "#DataResSaveBtn"
            input_wrapper = "[overlayid='DataResLists']"
            input_name = "#DataResField"
            input_empty = "div[overlayid='DataResLists'] .ant-select-selection-placeholder"
            input_selected = "div[overlayid='DataResLists'] .ant-select-selection-item"
            input_lists = "div[id='DataResLists'] .rc-virtual-list-holder-inner"
            input_item = "(//div[@id='DataResItem'])"

        class DataForm:
            """Data Diri"""
            info_main = "//div[contains(@class, 'importDataModalMain')]//div[@id='DataProfInfoSelfDataToggle']"   #"div[class]#DataProfInfoSelfDataToggle"
            info_toggle = "div[id='DataProfInfoSelfDataToggle'] div[role='button']"
            info_check = "//label[contains(@class,'SelfDataCheck')]//input"
            info_title = "#DataProfInfoSelfDataHeader"
            info_name = "#dataProfInfoSelfDataName"
            info_email = "#dataProfInfoSelfDataEmail"
            info_phone = "#dataProfInfoSelfDataPhone"
            info_prov = "#dataProfInfoSelfDataProvince"
            info_city = "#dataProfInfoSelfDataCity"

            """Riwayat Pendidikan"""
            edu_main = "#DataProfInfoEduToggle"
            edu_toggle = "div[id='DataProfInfoEduToggle'] div[role='button']"
            edu_title = "#DataProfInfoEduHeader"
            edu_name = "//span[contains(@id,'EduName')]"
            edu_country = ""
            edu_prov = ""
            edu_city = ""
            edu_faculty = ""
            edu_start = ""
            edu_end = ""
            edu_score = ""


class DataDiri:
    submit_btn = "#selfInfoSubmitBtn"
    title = "#selfInfoTitle"
    main_form = "#selfInfoToggle"
    form_state = "#selfInfoToggle .ant-collapse-header"

    class Initial:
        main_hint = "#selfInfoHint"
        hint_btn = "#selfInfoHintBtn"
        hint_title = "div[id='selfInfoHint'] strong"
        hint_desc = "#selfInfoHintDesc"
        first_name_label = "#selfInfoFirstNameLabel"
        first_name_input = "#selfInfoFirstNameInput"
        last_name_label = "#selfInfoLastNameLabel"
        last_name_input = "#selfInfoLastNameInput"
        email_label = "#selfInfoEmailLabel"
        email_input = "#selfInfoEmailInput"
        phone_label = "#selfInfoPhoneLabel"
        phone_input = "#selfInfoPhoneInput"
        country_label = "#selfInfoCountryLabel"
        country_input = "[name='country']"
        country_content = "div[name='country'] .ant-select-selection-item"
        country_lists = "#selfInfoCountryLists"
        country_wni = "#selfInfoCountryIndo"
        country_wna = "#selfInfoCountryNonIndo"
        province_label = "#selfInfoProvinceLabel"
        province_input = "//div[@name='province']//input"
        province_empty = "//div[@name='province']//span[contains(@class,'placeholder')]"
        province_selected = "//div[@name='province']//span[contains(@class,'item')]"
        province_lists = "#selfInfoProvinceList"
        province_item = "(//div[@id='selfInfoProvinceItem'])"
        city_label = "#selfInfoCityLabel"
        city_input = "#selfInfoCityInput"
        city_empty = "//div[@name='city']//span[contains(@class,'placeholder')]"
        city_selected = "//div[@name='city']//span[contains(@class,'item')]"
        city_lists = "#selfInfoCityList"
        city_item = "(//div[@id='selfInfoCityItem'])"
        address_label = "#selfInfoAddressLabel"
        address_input = "#selfInfoAddressInput"
        linkedin_label = "#selfInfoLinkedinLabel"
        linkedin_input = "#selfInfoLinkedinInput"
        portfolio_label = "#selfInfoPortfolioLabel"
        portfolio_input = "#selfInfoPortfolioInput"

    class Filled:
        save = "#infoSelfSave"
        edit = "#infoSelfEdit"
        delete = "#infoSelfDelete"
        wrapper = "//div[@id='selfInfoToggle']//div[@id='DataProfInfoSelfDataWrapper']"
        name = "div[id='selfInfoToggle'] #dataProfInfoSelfDataName"
        first_name = "div[id='selfInfoToggle'] #dataProfInfoSelfDataFirstName"
        last_name = "div[id='selfInfoToggle'] #dataProfInfoSelfDataLastName"
        email = "div[id='selfInfoToggle'] #dataProfInfoSelfDataEmail"
        phone = "div[id='selfInfoToggle'] #dataProfInfoSelfDataPhone"
        province = "div[id='selfInfoToggle'] #dataProfInfoSelfDataProvince"
        city = "div[id='selfInfoToggle'] #dataProfInfoSelfDataCity"
        address = "div[id='selfInfoToggle'] #dataProfInfoSelfDataAddress"
        linkedin = "div[id='selfInfoToggle'] #dataProfInfoSelfDataLinkedin"
        linkedin_checkbox = "div[id='selfInfoToggle'] #dataProfInfoSelfDataLinkedin-checkbox-fill"
        portfolio = "div[id='selfInfoToggle'] #dataProfInfoSelfDataPortfolio"
        portfolio_checkbox = "div[id='selfInfoToggle'] #dataProfInfoSelfDataPortfolio-checkbox-fill"

    class Preview:
        name = ".header-name"
        first_name = "#previewFirstName"
        last_name = "#previewLastName"
        phone = "#previewPhoneNumber"
        email = "#previewEmail"
        city = "#previewCity"
        province = "#previewProvince"
        linkedin = "#previewLinkedinUrl"
        portfolio = "#previewPortfolioUrl"
        address = "#previewAddress"


class EduHistory:
    add_btn = "#educationAdd"
    toggle = "div[id='educationToggle'] div[role='button']"
    title = "#educationTitle"
    description = "//div[@id='educationToggle']//span[contains(@class,'secondary')]"
    hint_main = "#educationHint"
    hint_title = "div[id='educationHint'] strong"
    hint_btn = "#educationHintBtn"
    hint_desc = "#educationHintDesc"
    degree_label = "#educationDegreeLabel"
    degree_input = "[overlayid='educationDegreeList']"
    degree_content = "div[overlayid='educationDegreeList'] .ant-select-selection-item"
    degree_lists = "#educationDegreeList"
    degree_sma = "//div[@id='educationDegreeItem' and contains(@title,'SMA')]"
    degree_d1 = "//div[@id='educationDegreeItem' and contains(@title,'D1')]"
    degree_d2 = "//div[@id='educationDegreeItem' and contains(@title,'D2')]"
    degree_d3 = "//div[@id='educationDegreeItem' and contains(@title,'D3')]"
    degree_d4 = "//div[@id='educationDegreeItem' and contains(@title,'D4')]"
    degree_s1 = "//div[@id='educationDegreeItem' and contains(@title,'S1')]"
    degree_s2 = "//div[@id='educationDegreeItem' and contains(@title,'S2')]"
    degree_s3 = "//div[@id='educationDegreeItem' and contains(@title,'S3')]"
    degree_course = "//div[@id='educationDegreeItem' and contains(@title,'Kursus')]"
    name_label = "#educationNameLabel"
    name_input = "#educationNameInput"
    name_empty = "div[name='education_name'] .ant-select-selection-placeholder"
    name_selected = "div[name='education_name'] .ant-select-selection-item"
    name_list = "//div[@id='educationNameList']//div[contains(@class, 'holder-inner')]"
    name_item = "(//div[@id='educationNameItem'])"
    name_add = "//div[@id='educationNameList']/div[contains(@class, 'addMenu')]"
    faculty_label = "#educationFacultyLabel"
    faculty_input = "#educationFacultyInput"
    faculty_list = "//div[@id='educationFacultyList']//div[contains(@class, 'holder-inner')]"
    faculty_add = "//div[@id='educationFacultyList']/div[contains(@class, 'addMenu')]"
    faculty_item = "(//div[@id='educationFacultyItem'])"
    faculty_empty = "div[name='education_faculty'] .ant-select-selection-placeholder"
    faculty_selected = "div[name='education_faculty'] .ant-select-selection-item"
    gpa_label = "#educationFinalScoreLabel"
    gpa_input = "#educationFinalScoreInput"
    gpa_increase = "(//span[@role='button' and contains(@class, 'up')])[1]"
    gpa_decrease = "(//span[@role='button' and contains(@class, 'down')])[1]"
    max_gpa_label = "#educationMaxFinalScoreLabel"
    max_gpa_input = "#educationMaxFinalScoreInput"
    max_gpa_increase = "(//span[@role='button' and contains(@class, 'up')])[2]"
    max_gpa_decrease = "(//span[@role='button' and contains(@class, 'down')])[2]"
    country_label = "#educationCountryLabel"
    country_input = "[name='education_country']"
    country_lists = "#educationCountryList"
    country_content = "div[name='education_country'] .ant-select-selection-item"
    country_wni = "#educationCountryIndo"
    country_wna = "#educationCountryNonIndo"
    province_label = "#educationProvinceLabel"
    province_input = "#educationProvinceInput"
    province_empty = "//div[@name='education_province']//span[contains(@class,'placeholder')]"
    province_selected = "//div[@name='education_province']//span[contains(@class,'item')]"
    province_lists = "#educationProvinceList"
    province_item = "(//div[@id='educationProvinceItem'])"
    city_label = "#educationCityLabel"
    city_input = "#educationCityInput"
    city_empty = "//div[@name='education_city']//span[contains(@class,'placeholder')]"
    city_selected = "div[name='education_city'] .ant-select-selection-item"
    city_lists = "#educationCityList"
    city_item = "(//div[@id='educationCityItem'])"
    start_label = "#educationStartLabel"
    start_input = "#educationStartInput"
    start_clear = "//input[@id='educationStartInput']/following-sibling::span[contains(@class, 'picker-clear')]"
    end_label = "#educationEndLabel"
    end_input = "#educationEndInput"
    end_clear = "//input[@id='educationEndInput']/following-sibling::span[contains(@class, 'picker-clear')]"
    end_status = "//div[contains(@class, 'EducationForm')]"
    end_status_check = "//div[contains(@class, 'EducationForm')]//input[@name='is_present']"
    save_btn = "#educationFormSave"
    cancel_btn = "#educationFormCancel"

    """Filled State"""
    fill_education_item = "//div[contains(@class,'education-item')]"
    fill_name = "#dataProfInfoEduName"
    fill_country = "#dataProfInfoEduLocCountry"
    fill_province = "#dataProfInfoEduLocProvince"
    fill_city = "#dataProfInfoEduLocCity"
    fill_degree = "#dataProfInfoEduDetailsDegree"
    fill_faculty = "#dataProfInfoEduDetailsFaculty"
    fill_start = "#dataProfInfoEduDetailsStart"
    fill_end = "#dataProfInfoEduDetailsEnd"
    fill_score_checkbox = "#dataProfInfoEduScoreCheckBox"
    fill_final_score = "#dataProfInfoEduFinalScore"
    fill_max_score = "#dataProfInfoEduMaxScore"
    fill_education_description_item = "//div[contains(@class,'education-description-item')]"
    fill_education_description_add = "#educationDescriptionAdd"


class JobHistory:
    add_btn = "#addOccupation"
    toggle = "div[id='occupationToggle'] div[role='button']"
    title = "#occupationTitle"
    description = "#addOccupationText"
    hint_main = "#occupationHint"
    hint_title = "div[id='occupationHint'] strong"
    hint_btn = "#occupationHintBtn"
    hint_desc = "#occupationHintDesc"
    pos_input = "#occupationPositionInput"
    pos_label = "label[title='Posisi']"
    pos_empty = "div[name='occupation_position'] .ant-select-selection-placeholder"
    pos_selected = "div[name='occupation_position'] .ant-select-selection-item"
    pos_list = "//div[@id='occupationPositionList']//div[contains(@class,'holder-inner')]"
    pos_add = "//div[@id='occupationPositionList']//div[contains(@class,'addMenu')]"
    pos_item = "(//div[@id='occupationPositionItem'])"
    company_label = "#companyNameLabel"
    company_input = "#companyNameInput"
    country_label = "#companyCountryLabel"
    country_input = "[name='company_country']"
    country_content = "div[name='company_country'] .ant-select-selection-item"
    country_lists = "#companyCountryList"
    country_wni = "#occupationCountryIndo"
    country_wna = "#occupationCountryNonIndo"
    province_label = "#companyProvinceLabel"
    province_input = "#companyProvinceInput"
    province_empty = "//div[@name='company_province']//span[contains(@class,'placeholder')]"
    province_selected = "//div[@name='company_province']//span[contains(@class,'item')]"
    province_lists = "#companyProvinceList"
    province_item = "(//div[@id='companyProvinceItem'])"
    city_label = "#companyCityLabel"
    city_input = "#companyCityInput"
    city_empty = "//div[@name='company_city']//span[contains(@class,'placeholder')]"
    city_selected = "div[name='company_city'] .ant-select-selection-item"
    city_lists = "#companyCityList"
    city_item = "(//div[@id='companyCityItem'])"
    status_label = "#occupationStatusLabel"
    status_input = "#occupationStatusInput"
    status_content = "div[overlayid='occupationStatusList'] .ant-select-selection-item"
    status_lists = "#occupationStatusList"
    status_full = "//div[@id='occupationStatusItem' and contains(@title,'Purnawaktu')]"
    status_part = "//div[@id='occupationStatusItem' and contains(@title,'Paruh Waktu')]"
    status_freelance = "//div[@id='occupationStatusItem' and contains(@title,'Pekerja Lepas')]"
    status_intern = "//div[@id='occupationStatusItem' and contains(@title,'Magang')]"
    status_volunteer = "//div[@id='occupationStatusItem' and contains(@title,'Sukarela')]"
    start_label = "#occupationStartLabel"
    start_input = "#occupationStartInput"
    start_clear = "//input[@id='occupationStartInput']/following-sibling::span[contains(@class, 'picker-clear')]"
    end_label = "#occupationEndLabel"
    end_input = "#occupationEndInput"
    end_status = "//div[contains(@class, 'OccupationForm')]"
    end_status_check = "//div[contains(@class, 'OccupationForm')]//input[@id='id1']"
    end_clear = "//input[@id='occupationEndInput']/following-sibling::span[contains(@class, 'picker-clear')]"
    form_cancel = "#occupationFormCancel"
    form_save = "#occupationFormSave"


class Proficiency:
    title = "#proficiencyTitle"
    toggle = "div[id='proficiencyToggle'] div[role='button']"
    add_btn = "#addProficiency"
    description = "#addProficiencyText"
    form = "#proficiencyToggle"
    hint_main = "#proficiencyHint"
    hint_btn = "#proficiencyHintBtn"
    hint_title = "div[id='proficiencyHint'] strong"
    hint_desc = "#proficiencyHintDesc"
    name_label = "#proficiencyNameLabel"
    name_input = "#proficiencyNameInput"
    level_label = "#proficiencyLevelLabel"
    level_input = "[name='proficiency_level']"
    level_content = "div[name='proficiency_level'] .ant-select-selection-item"
    level_lists = "#proficiencyLevelList"
    level_item_pemula = "//div[@id='proficiencyLevelItem' and @title='Pemula']"
    level_item_menengah = "//div[@id='proficiencyLevelItem' and @title='Menengah']"
    level_item_lanjut = "//div[@id='proficiencyLevelItem' and @title='Lanjut']"
    form_cancel = "#proficiencyFormCancel"
    form_save = "#proficiencyFormSave"


class Achievements:
    form = "#achievementToggle"
    title = "#achievementTitle"
    description = "#addAchievementText"
    add_btn = "#addAchievement"
    toggle = "div[id='achievementToggle'] div[role='button']"
    hint_main = "#achievementHint"
    hint_title = "div[id='achievementHint'] strong"
    hint_btn = "#achievementHintBtn"
    hint_desc = "#achievementHintDesc"
    year_label = "#achievementYearLabel"
    year_input = "#achievementYearInput"
    year_clear = "//input[@id='achievementYearInput']/following-sibling::span[contains(@class, 'picker-clear')]"
    name_label = "#achievementNameLabel"
    name_input = "#achievementNameInput"
    form_cancel = "#achievementFormCancel"
    form_save = "#achievementFormSave"


class Hobby:
    form = "#hobbiesToggle"
    title = "#hobbiesTitle"
    desc = "#addInterestText"
    toggle = "div[id='hobbiesToggle'] div[role='button']"
    add_btn = "#addInterest"
    hint_main = "#hobbyHint"
    hint_btn = "#hobbyHintBtn"
    hint_title = "div[id='hobbyHint'] strong"
    hint_desc = "#hobbyHintDesc"
    name_label = "#hobbyNameLabel"
    name_input = "#hobbyNameInput"
    form_cancel = "#hobbyFormCancel"
    form_save = "#hobbyFormSave"


class Preview:
    main = "#resume-preview"
    section_title = "#previewLayoutTitle"
    completeness = "//div[contains(@class, 'previewLayout')]//span//strong"
    complete_tag = "#resumeStatusTag"
