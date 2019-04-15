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

    def check_error_tip(self):
        global check_res
        check_res = False
        i = 0
        while i < 5:
            error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
            if Common.check_text_in_list(self, error_list, "验证码输入错误"):
                check_res = True
                break
            i += 1
            Common.wait(self, 1)

    def test_step(self):
        u"""输入错误的验证码"""
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        Common.wait(self, 10)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])
        logger.info("输入手机号")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       "19802990115")

        logger.info("点击获取验证码,判断是否出现错误提示")
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)

        logger.info("输入错误的验证码，点击确定，查看错误提示")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码",
                                                       "123456")
        threading.Thread(target=self.check_error_tip, args=()).start()
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)
        self.assertTrue(check_res)




