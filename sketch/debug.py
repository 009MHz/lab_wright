import json

def loader():
    with open(r"resources\data\url_routing.json", "r") as source:
        raw = json.load(source)
        return raw

def select_enviro(page:None, env, type:None):
    for base_page in source:
        for selected_page in base_page:  # page = karirlab / employers
            # print(f"Selected Page: {selected_page}")
            if selected_page == page:
                for item in base_page[page]:  # item = prod / staging
                    for enviro, content in item.items():
                        if enviro == env:
                            # print(f"Content: {content}")
                            for account_type in content:
                                # print(f"Account type: {account_type}")
                                for url_mode, url_value in account_type.items():
                                    # print(f"Mode: {mode}")
                                    if url_mode == type:
                                        return url_value
                
print(select_enviro(page="karirlab", env="staging", type="user"))

