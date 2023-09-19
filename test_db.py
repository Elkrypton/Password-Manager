
from database import *
from sqlalchemy.exc import IntegrityError
import pytest

class TestPasswordDatabase():

    def setup_method(self):
        self._session = load_engine()
        self.valid_login = ProcessInformation(website='test',email="test@example.com",hashed="gAAAAABlB60gzBlgCmNUNLpLx7P4UxVSqCjJ6IXiJ6eT0wAaUOEgTyvRJaDbywvE-ElXFh04hPK6yRVebOyrVh19lcdyB7_Z2g==")
        self.valid_login.add_data()

    
    def teardown_method(self):
        self._session.rollback()
        self._session.close()


    @pytest.mark.xfail(raises=TypeError)
    def test_login_no_email(self):
        login_info = ProcessInformation(website="Fcb",hashed="gAAAAABlB60gzBlgCmNUNLpLx7P4Ux")
        try:
            login_info.add_data()
        except Exception:
            self._session.rollback()

    def test_login_valid(self):

        validate = self._session.query(LoginInfo).filter(LoginInfo.website=='test').one()
        assert validate.email == "test@example.com"
        assert validate.hashed ==  "gAAAAABlB60gzBlgCmNUNLpLx7P4UxVSqCjJ6IXiJ6eT0wAaUOEgTyvRJaDbywvE-ElXFh04hPK6yRVebOyrVh19lcdyB7_Z2g=="
    
    def test_update(self):
        status = UpdateData('test', 'gAAAAABlB60gzBlgCmNUNLpLx7P4UxVSqCjJ6IXiJ6eT0wAaUOEgTyvRJaDbywvE-ElXFh04hPK6yRVebOyrVh19lcdyB7_Z2g==')
        assert status == True

    def test_delete(self):
        status = DeleteOneEntry(123)
        assert status == True
