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
        u"""安卓-垃圾箱-搜索功能"""
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

        logger.info("创建一个草稿")
        Mail_phone.creat_draft(self, Content.spare_mail_address, "mail_theme_1", mail_content="123")
        Mail_phone.creat_draft(self, Content.spare_mail_address, "mail_theme_2", mail_content="456")
        Mail_phone.creat_draft(self, Content.spare_mail_address, "mail_theme_3", mail_content="789")

        logger.info("创建垃圾邮件")
        Mail_phone.creat_dustbin_from_other_place(self, "草稿箱", "mail_theme_1", "mail_theme_2", "mail_theme_3")

        logger.info("进入垃圾箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_dustbin)

        logger.info("查看草稿是否存在")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertTrue(BaseOperate.check_text_in_list(self, theme_list, "mail_theme_1"))
        self.assertTrue(BaseOperate.check_text_in_list(self, theme_list, "mail_theme_2"))
        self.assertTrue(BaseOperate.check_text_in_list(self, theme_list, "mail_theme_3"))

        logger.info("查看垃圾箱信息是否显示完整")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_send_account))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_theme))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_content))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_time))

        logger.info("进行搜索")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "mail_theme_1")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("查看是否搜索成功")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertTrue(BaseOperate.check_text_in_list(self, theme_list, "mail_theme_1"))


 
     
