#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % Content.register_count, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.report_template_user_rl WHERE user_id='%s'" % id, "scap")
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓点击模板进入模板"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP，进入主界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入服务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayoutid_homeLayout)

        logger.info("进入可视化界面")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "可视化")
        Common.wait(self, 5)

        logger.info("判断是否进入可视化界面")
        title = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(title, "数据可视化")

        logger.info("将模板设为常用")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "全部模板")
        disign = BaseOperate.get_results_by_id(self, PhoneControl.id_oper)
        BaseOperate.touch_by_element(self, disign[0])
        disign1 = BaseOperate.get_results_by_id(self, PhoneControl.id_oper)
        self.assertEqual(len(disign), len(disign1)+1)


