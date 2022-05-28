    def test_nonexist_user_login(self, app):
        user = RegisterModel.random()
        login_response = app.login.login_user(data=user, )
        assert res_login.status_code == 401
        assert login_response.data.description == "Invalid credentials"
        assert login_response.data.error == "Bad Request"