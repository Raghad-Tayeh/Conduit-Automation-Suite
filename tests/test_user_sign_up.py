from data_feeders import sign_up_data_feeder as data_feeder
from pages import sign_up_page as signup_page

def test_user_can_sign_up(browser_launch):
    data = data_feeder.sign_up_feeder()
    signup_obj = signup_page.SignUpPage(browser_launch)
    signup_obj.signup(data["username"], data["email"], data["password"])
