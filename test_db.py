
from database import *

class TestPasswordManager():

    def setup_method(self):
        self._session = load_engine()

    def test_login_valid(self):

        validate = self._session.query(LoginInfo).filter(LoginInfo.website=='test').one()
        assert validate.email == "test@example.com"
        assert validate.hashed ==  "gAAAAABlB60gzBlgCmNUNLpLx7P4UxVSqCjJ6IXiJ6eT0wAaUOEgTyvRJaDbywvE-ElXFh04hPK6yRVebOyrVh19lcdyB7_Z2g=="
    
    def test_update(self):
        status = UpdateData('test', 'gAAAAABlB60gzBlgCmNUNLpLx7P4UxVSqCjJ6IXiJ6eT0wAaUOEgTyvRJaDbywvE-ElXFh04hPK6yRVebOyrVh19lcdyB7_Z2g==')
        assert status == True