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
        BaseOperate.delete_meeting_record(self, Content.spare_count)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—创建人取消会议"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

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

        logger.info("点击进入会议详情, 查看右上角“...”是否存在")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)
        sign_btn = BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_btn)
        self.assertTrue(sign_btn)

        logger.info("点击右上角“...”")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击取消会议")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "取消会议")

        logger.info("输入取消会议的原因, 点击确定")
        BaseOperate.sendTextById(self, PhoneControl.id_input, "cancel_reason")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("查看是否取消成功")
        status = BaseOperate.get_text_by_id(self, PhoneControl.id_status)
        self.assertEqual(status, "已取消")


 
     
