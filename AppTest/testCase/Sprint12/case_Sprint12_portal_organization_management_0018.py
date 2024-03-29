#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.delete_department_by_name(self, "zs_test")
        Common.quit(self)

    def test_step(self):
        u"""pc-添加部门成员，手机号与职位输入长度限制"""
        logger.info("登录后端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "新建部门", "button")

        logger.info("输入一个存在与系统中的主管账号")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "新建部门", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入部门名称", "zs_test")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入部门主管手机号码",
                                                       Content.register_count)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看是否可以创建成功")
        department_name = Common.get_result_by_class_name(self, ClassName.department)
        name_ele_list = Common.get_class_name_elements_by_element(self, department_name, ClassName.name)
        name_list = Common.get_text_by_elements(self, name_ele_list)
        self.assertTrue(Common.check_text_in_list(self, name_list, "zs_test"))

        logger.info("点击添加人员")
        Common.touch_text_by_class_name(self, ClassName.name, "zs_test", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加人员", "button")
        header = Common.get_text_by_class_name(self, ClassName.ivu_modal_header_inner, "div")
        self.assertTrue(Common.check_text_in_list(self, header, "添加人员"))

        logger.info("点击查看重命名时，输入长度限制")
        ele_1 = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入手机号码")
        self.assertEqual(ele_1.get_attribute("maxlength"), "50")



