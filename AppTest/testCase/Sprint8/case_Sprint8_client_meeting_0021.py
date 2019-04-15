#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.delete_meeting_record(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""与会人签到时间后会议开始前未点击确认时点击未结束的会议，点击确认"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "会议", "p")

        logger.info("判断是否进入会议界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.addMeetingBtn))

        logger.info("创建一个会议")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        Common.creat_meeting(self, "meeting_theme", name=real_name)

        logger.info("通过后台修改会议时间")
        start_time, end_time = Common.get_start_and_end_time(self)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_theme", Content.register_count)

        logger.info("登录参会人账号")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "会议", "p")

        logger.info("进入会议详情界面")
        Common.open_meeting_detail_by_name(self, "meeting_theme", 1)

        logger.info("查看‘确认参加’与‘不参加’按钮是否存在")
        self.assertTrue(Common.check_if_id_exist(self, ID.notAttendBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.attendBtn))

        logger.info("点击确认")
        Common.touch_by_id(self, ID.attendBtn)

        logger.info("出现可点击的签到按钮")
        self.assertTrue(Common.check_if_id_exist(self, ID.signMeetingBtn))
        self.assertEqual(Common.get_text_by_element(self, Common.get_result_by_id(self, ID.signMeetingBtn)), "会议签到")


 
     
