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
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-发件箱-编辑模式搜索验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击首页, 进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("判断是否进入邮箱界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "邮箱")

        logger.info("进入我的邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_my_mail)

        logger.info("发送邮件")
        Mail_phone.send_mail(self, Content.spare_mail_address, "mail_theme_1")
        Mail_phone.send_mail(self, Content.spare_mail_address, "mail_theme_2")
        Mail_phone.send_mail(self, Content.spare_mail_address, "mail_theme_3")

        logger.info("进入发件箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_send_box)
        theme_list_all = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertEqual(len(theme_list_all), 3)

        logger.info("点击编辑")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("点击搜索")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "mail_theme_1")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("查看是否可以搜索成功")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertEqual(len(theme_list), 1)
        theme = BaseOperate.get_text_by_id(self, PhoneControl.id_theme)
        self.assertEqual(theme, "mail_theme_1")


 
     
