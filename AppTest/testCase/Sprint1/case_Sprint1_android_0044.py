#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击设置生日")
        BaseOperate.touch_id_by_index(self, PhoneControl.my_data_birthday)

        logger.info("点击取消")
        BaseOperate.touch_id_by_index(self, PhoneControl.my_data_birthday_cancel)

        logger.info("检测取消是否存在")
        statue = BaseOperate.checkIfIdExist(self, PhoneControl.id_content_container)
        self.assertFalse(statue)



    
