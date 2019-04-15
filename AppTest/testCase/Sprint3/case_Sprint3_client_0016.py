#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""web手机号码输入英文字符"""
        logger.info("电话号码前面存在英文特殊字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       "$"+Content.register_count)
        Common.touch_by_id(self, ID.handleSubmitBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, error_list, "您的手机号码输入错误"))

        logger.info("电话号码中间存在英文特殊字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", "19802990$115")
        Common.touch_by_id(self, ID.handleSubmitBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, error_list, "您的手机号码输入错误"))



     
