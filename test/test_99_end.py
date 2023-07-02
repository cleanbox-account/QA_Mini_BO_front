# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.07
# version ='1.0'
# ---------------------------------------------------------------------------
from utilsModules.Logs_input import input_logs


class TestStart():
    test_dir = "test"    
    def test_FINISH_TEST_CYCLE(self):
        title = 'Mini BACKOFFICE UI - FINISH TEST CYCLE'
        
        input_logs("INFO", "* "*50, self.test_dir)
        input_logs("INFO", "* *"+" "*10 + title + " "*(83-len(title)) + "* *", self.test_dir)
        input_logs("INFO","* "*50, self.test_dir)
        input_logs("---", "", self.test_dir)