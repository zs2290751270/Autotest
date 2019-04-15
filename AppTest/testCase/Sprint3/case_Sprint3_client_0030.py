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
        u"""web已用过一次验证码"""
        logger.info("点击注册")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_offset_19, "注册账号", "div")

        logger.info("输入手机号码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "设置常用手机号为登录账号",
                                                       Content.no_register_count)

        logger.info("输入登录密码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "设置6位以上数字字母组合的密码",
                                                       Content.login_password)

        logger.info("点击同意用户协议")
        user_procotol = Common.get_result_by_class_name_blank(self, "input", ClassName.ivu_checkbox_input)
        Common.touch_by_element(self, user_procotol)

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.getRegisterCodeBtn)

        logger.info("获取验证码")
        identify_code = Common.get_identifying_code(self, Content.no_register_count)
        Common.wait(self, 30)
        Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码")
        Common.wait(self, 30)
        logger.info("再次点击获取验证码")
        Common.touch_by_id(self, ID.getRegisterCodeBtn)

        logger.info("输入特殊字符作为验证码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", identify_code)

        logger.info("点击注册")
        threading.Thread(target=self.check_error_tip, args=()).start()
        Common.touch_by_id(self, ID.registerBtn)
        self.assertTrue(check_res)




