*** Settings ***
Library        SeleniumLibrary

*** Variables ***

#Header section
${input_resume_name}       id:title
${select_language}         xpath:("(//input[@id='id1'])[1]")
${job_objective}           xpath:("(//input[@id='id1'])[2]")
${header_section}    ${input_resume_name}    ${select_language}    ${job_objective}


#Import Data section
${btn_import}              xpath://button[contains(., 'Impor Data')]
${btn_close}               class:ant-modal-close-icon
${btn_from_profile}        xpath:("//button[contains(., 'Impor dari profil saya')]")
${btn_from_resume}         xpath:("//button[contains(., 'Impor dari resume saya')]")

#Personal Information section
${btn_personal}            xpath://button[contains(., 'Data Diri')]
${input_first_name}        id:first_name
${input_last_name}         id:last_name
${input_email}             id:last_name
${input_handphone}         id:phone_number
${selector_country}        xpath:("(//input[@id='id1'])[3]")
${selector_province}       xpath:("(//input[@id='id1'])[4]")
${selector_city}           xpath:("(//input[@id='id1'])[5]")
${input_address}           id:address
${input_linkedin}          id:linkedin_url
${input_portfolio}         id:portfolio_url
${btn_cancel_personal}     xpath://button[contains(., 'Batal')]
${btn_save_personal}       xpath://button[contains(., 'Simpan')]

#Education section
${btn_education}           xpath://button[contains(., 'Riwayat Pendidikan')]
${selector_degree}         xpath:("(//input[@id='id1'])[3]")
${selector_institution}    xpath:("(//input[@id='id1'])[4]")
${selector_major}          xpath:("(//input[@id='id1'])[5]")
${input_gpa}               xpath:("//input[@id='education_final_score']")
${input_max_gpa}           xpath:("//input[@id='education_max_score']")
${selector_country}        xpath:("(//input[@id='id1'])[6]")
${selector_province}       xpath:("(//input[@id='id1'])[7]")
${selector_city}           xpath:("(//input[@id='id1'])[8]")
${datetepicker_start}      xpath:("(//input[@id='id1'])[9]")
${datepicker_end}          xpath:("(//input[@id='id1'])[10]")
${checkbox_active}         class:ant-checkbox-input
${btn_cancel_education}    xpath://button[contains(., 'Batal')]
${btn_save_education}      xpath://button[contains(., 'Simpan')]

#Occupation section
${btn_occupation}          xpath://button[contains(., 'Riwayat Pekerjaan')]
${selector_position}       xpath:("(//input[@id='id1'])[3]")
${input_company}           id:company_name
${selector_country}        xpath:("(//input[@id='id1'])[4]")
${selector_province}       xpath:("(//input[@id='id1'])[5]")
${selector_city}           xpath:("(//input[@id='id1'])[6]")
${selector_status}         xpath:("(//input[@id='id1'])[7]")
${datetepicker_start}      xpath:("(//input[@id='id1'])[8]")
${datepicker_end}          xpath:("(//input[@id='id1'])[9]")
${checkbox_active}         class:ant-checkbox-input
${btn_cancel_occupation}   xpath://button[contains(., 'Batal')]
${btn_save_occupation}     xpath://button[contains(., 'Simpan')]


#Skill section
${btn_skill}               xpath://button[contains(., 'Keahlian')]
${input_skill}             id:proficiency_name
${selector_grade}          xpath:("(//input[@id='id1'])[3]")
${btn_cancel_skill}        xpath://button[contains(., 'Batal')]
${btn_save_skill}          xpath://button[contains(., 'Simpan')]

#Awards section
${btn_award}               xpath://button[contains(., 'Prestasi & Penghargaan')]
${datepicker_year}         xpath:("(//input[@id='id1'])[3]")
${input_awards}            id:achievement_name
${btn_cancel_awards}       xpath://button[contains(., 'Batal')]
${btn_save_awards}         xpath://button[contains(., 'Simpan')]

#Interest section
${btn_interest}            xpath://button[contains(., 'Minat')]
${input_hobby}             id:hobby_name
${btn_cancel_hobby}        xpath://button[contains(., 'Batal')]
${btn_save_hobby}          xpath://button[contains(., 'Simpan')]

#Button Save
${btn_save_resume}         xpath://button[contains(., 'Simpan Resume')]