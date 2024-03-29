#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        # BaseOperate.uninstallApp(self, PhoneControl.package_name)
        # BaseOperate.quit(self)

    def test_step(self):
        u"""输入正确的手机号码，密码输错，点击登录三次，输入错误的图形验证码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面,输入账号")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.sendTextById(self, PhoneControl.login_count, phoneNum)

        logger.info("输入错误的密码，点击三次登录")
        BaseOperate.sendTextById(self, PhoneControl.login_password, "qweqwe123")
        for i in range(1, 4):
            logger.info("第%s次开始" % i)
            BaseOperate.touch_id_by_index(self, PhoneControl.login_login_button)
            BaseOperate.wait(self, 1)

        logger.info("判断是否出现验证码,第三次点击")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_verify_code_iv))



