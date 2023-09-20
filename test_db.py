
from database import *
from sqlalchemy.exc import IntegrityError
import pytest
from password_manager import PasswordManager
from utils import CryptTools


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

class TestPasswordManagerInterface():

    def setup_method(self):
        self.password_manager = PasswordManager("test","test","test")
    

    def test_valid_info(self):
        assert self.password_manager.website == "test"
        assert self.password_manager.email == "test"
        assert self.password_manager.password == "test"
    

    def test_save_password(self):
        assert self.password_manager.SavePassword() == True
    

    

class TestCryptography():
    def setup_method(self):
        self.encryption_obj = CryptTools('test').Encrypt()
        self.encryption_obj_2 = CryptTools('test').Encrypt()
        self.decryption_obj = CryptTools(self.encryption_obj.decode()).Decrypt()
    
    def test_decrypt(self):
        
        decrypted_text = self.decryption_obj
        assert decrypted_text == b'test'
    
    def test_encryption_changes(self):
        assert self.encryption_obj != self.encryption_obj_2
    
