from service.testcase import Testcase


class Test_testcase:

    def setup(self):
        self.testcase = Testcase()

    def test_get(self):
        t = self.testcase.get()
        print(t)

    def test_create(self):
        t = self.testcase.create(id=6, case_title='测试用例006', remark='备注006')
        print(t)


    def test_delete(self):
        t = self.testcase.delete(id=7)
        print(t)

    def test_update(self):
        t = self.testcase.update(id=6, case_title='测试用例', remark='备注')
        print(t)