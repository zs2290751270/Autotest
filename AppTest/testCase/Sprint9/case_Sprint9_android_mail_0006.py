#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


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
        Mail.del_mail_record_by_user(self, Content.register_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-邮箱首页-滑动屏幕"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("判断是否进入邮箱界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "邮箱")

        logger.info("进入我的邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_my_mail)

        logger.info("发送邮件")
        Mail_phone.send_mail(self, Content.spare_mail_address, "theme_1")
        Mail_phone.send_mail(self, Content.spare_mail_address, "theme_2")
        Mail_phone.send_mail(self, Content.spare_mail_address, "theme_3")
        Mail_phone.send_mail(self, Content.spare_mail_address, "theme_4")

        logger.info("切换账号")
        BaseOperate.app_login_out(self)
        BaseOperate.app_login(self, Content.spare_count, Content.spare_password)

        logger.info("辅助账号进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("查看邮件是否接收成功")
        self.assertTrue(Mail_phone.check_mail_if_exist_by_theme(self, "theme_1"))
        self.assertTrue(Mail_phone.check_mail_if_exist_by_theme(self, "theme_2"))
        self.assertTrue(Mail_phone.check_mail_if_exist_by_theme(self, "theme_3"))
        self.assertTrue(Mail_phone.check_mail_if_exist_by_theme(self, "theme_4"))

        logger.info("搜索邮件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "theme_1")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("点击搜索")
        theme_1 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertTrue(BaseOperate.check_text_in_list(self, theme_1, "theme_1"))
        self.assertTrue(len(theme_1), 1)


 
     
