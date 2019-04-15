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
        u"""创建人会议详情界面会议开始前修改会议参会人弹出框测试搜索"""
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
        realname = Common.get_realname_by_phone(self, Content.spare_count)
        Common.creat_meeting(self, "meeting_theme", name=realname)

        logger.info("修改会议时间")
        start_time, end_time = Common.get_start_and_end_time(self, time_len=10)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_theme", Content.register_count)

        logger.info("点击修改会议")
        Common.open_meeting_detail_by_name(self, "meeting_theme")
        Common.touch_by_id(self, ID.editMeetingBtn)
        add_person = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, add_person, "img")

        logger.info("查看是否可以搜索")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号或者姓名",
                                                       Content.spare_count)
        check_box = Common.get_result_by_class_name_blank(self, "input", ClassName.ivu_checkbox_input)
        self.assertEqual(check_box.get_attribute("disabled"), "true")


 
     
