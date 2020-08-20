import unittest
import sys
sys.path.insert(1, "..")
from add_vhost_5.Checking_Steps_Result import Checking_Steps_Result


class test_Checking_Steps_Result(unittest.TestCase):

    def setUp(self):
        self.checking_steps_result = Checking_Steps_Result()

    def test_setOkAndGetResult(self):
        self.checking_steps_result.setOk()
        expected_dict = {
            "status": "Ok",
            "message": ""
        }
        self.assertDictEqual(expected_dict, self.checking_steps_result.getResponseResult())

    def test_setPartialAndGetResult(self):
        self.checking_steps_result.setPartial()
        expected_dict = {
            "status": "Partial",
            "message": ""
        }
        self.assertDictEqual(expected_dict, self.checking_steps_result.getResponseResult())


    def test_setProblemAndGetResult(self):
        self.checking_steps_result.setProblem()
        expected_dict = {
            "status": "Problem",
            "message": ""
        }
        self.assertDictEqual(expected_dict, self.checking_steps_result.getResponseResult())

    def test_setOkFluentInterface(self):
        returned_obj = self.checking_steps_result.setOk()
        self.assertTrue(isinstance(returned_obj, Checking_Steps_Result))

    def test_setPartialFluentInterface(self):
        returned_obj = self.checking_steps_result.setPartial()
        self.assertTrue(isinstance(returned_obj, Checking_Steps_Result))

    def test_setProblemFluentInterface(self):
        returned_obj = self.checking_steps_result.setProblem()
        self.assertTrue(isinstance(returned_obj, Checking_Steps_Result))

    def test_setMessageFluentInterface(self):
        returned_obj = self.checking_steps_result.setMessage("Some message")
        self.assertTrue(isinstance(returned_obj, Checking_Steps_Result))

    def test_setPartialAndMessage(self):
        returning_data = self.checking_steps_result.setPartial().setMessage("The file exists, but have no permission to write.").getResponseResult()
        expected_dict = {
            "status": "Partial",
            "message": "The file exists, but have no permission to write."
        }
        self.assertDictEqual(expected_dict, returning_data)
