from common.deco import log
from fixtures.register.model import RegisterModel
from fixtures.validator import Validator


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = '/user_info/{}'

    @log('Register new user')
    def add_user_info(self, user_id: int, data: RegisterModel, header=None, type_response=LoginUserResponse):
        # res = requests.post(f"{self.app.url}{self.POST_REGISTER}",
        #                     json=data.to_dict())
        res = self.app.client.request('POST', f"{self.app.url}{self.POST_REGISTER}",
                            json=data.to_dict())
        return self.structure(res, type_response)