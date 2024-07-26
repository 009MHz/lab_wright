class LogInLoc:
    url = "https://staging.karirlab.co/login"

    main_title = "//div//h3"
    email_label = "[for='username']"
    email_input = "#username"
    email_blank_warning = ""
    email_unregistered_warning = ""
    email_unregistered_cta = ""
    email_invalid_warning = ""

    pass_label = "[for='password']"
    pass_input = "#password"
    pass_eye_icon = "//span[contains(@class, 'eye')]"

    pass_blank_warning = ""
    forget_pass = "//a[contains(.,'Sandi')]"
    
    button_submit = "//button[contains(@class, 'submit')]"

    new_account_message = "//span[contains(@class, 'signUp')]"
    new_account_cta = f"{new_account_message}//a"

    btn_google_sso = "//button[contains(@class, 'google')]"
