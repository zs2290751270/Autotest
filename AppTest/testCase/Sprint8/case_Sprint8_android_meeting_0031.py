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
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.delete_meeting_record(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—修改会议界面返回按钮"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.creat_meeting(self, "meeting_test", "content", "area")

        logger.info("进行修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 5)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test", Content.register_count)

        logger.info("判断会议是否创建成功")
        title_name = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        check_res111 = BaseOperate.check_text_in_list(self, title_name, "meeting_test")
        self.assertTrue(check_res111)

        logger.info("进入会议详情界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("判断是否进入会议详情")
        text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_con, "会议详情")

        logger.info("判断会议是否可以进行操作,可以进行操作")
        check_res = BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_btn)
        self.assertTrue(check_res)

        logger.info("点击编辑会议")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "修改会议")

        logger.info("判断是否进入编辑会议界面")
        text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_con, "编辑会议")

        logger.info("点击返回")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)

        logger.info("判断是否返回会议详情")
        text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_con, "会议详情")


 
     
