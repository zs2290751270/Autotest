#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"


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
        BaseOperate.del_cloud_file_by_user(self, Content.register_count)
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.clear_window_local_file(self)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""文件下载"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建一个可上传的文件")
        BaseOperate.creat_file_in_android(self, "zhangsen_file.txt", folder_name, "zhangsen_test_file_content")

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "zhangsen_file.txt")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)

        logger.info("点击“...”，点击下载文件")
        BaseOperate.touch_more_by_name_in_cloud(self, "zhangsen_file.txt")
        BaseOperate.touch_text_by_id(self, "下载", PhoneControl.id_text)
        BaseOperate.touch_more_by_name_in_cloud(self, "zhangsen_file.txt")
        BaseOperate.touch_text_by_id(self, "下载", PhoneControl.id_text)

        logger.info("点击进入下载列表，查看是否下载成功,新下载的文件会覆盖源文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_downloaded_title)
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        logger.info(name_list)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "zhangsen_file.txt"))


 
     
