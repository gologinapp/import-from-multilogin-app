from library import Multilogin, GoLogin
from config import MULTILOGIN_TOKEN, MULTILOGIN_PORT, GOLOGIN_TOKEN

SUCCESS_MIGRATE = 0
ERROR_MIGRAGE = 0

multilogin = Multilogin(MULTILOGIN_TOKEN, MULTILOGIN_PORT)
multilogin_profiles = multilogin.get_profiles()

for profile in multilogin_profiles:
    multilogin_profile_data_dict = multilogin.get_profile_info(profile['uuid'])
    gologin = GoLogin(GOLOGIN_TOKEN)
    response = gologin.create_profile(multilogin_profile_data_dict)
    
    if response.status_code == 201:
        print('Profile', multilogin_profile_data_dict.get('name'), 'successfully created')
        SUCCESS_MIGRATE += 1
    else:
        print('Profile', multilogin_profile_data_dict.get('name'), 'Error!')
        print(f'Response is {response.text}')
        ERROR_MIGRAGE += 1

print(f'Count of profiles: {len(multilogin_profiles)}\nSuccess migrate: {SUCCESS_MIGRATE}\nError migrate: {ERROR_MIGRAGE}')

# For migrate single profile
# for profile in multilogin_profiles:
#     if 'NaMe Of PrOfiLe' in profile.values():
#         print(f'pofile is {profile}\n')      
#         multilogin_profile_data_dict = multilogin.get_profile_info(profile['uuid'])
#         print(f'gologin request {multilogin_profile_data_dict}')
#         gologin = GoLogin(GOLOGIN_TOKEN)
#         response = gologin.create_profile(multilogin_profile_data_dict)
#         print(f'response text {response.text}')

print('Migration process completed')

