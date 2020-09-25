import requests

from api_tag_requests.api_tag.tag import Tag
from api_tag_requests.api_tag.wework import WeWork


class TestTag:
    def setup_class(self):
        # 实例化WeWork()，获取access_token
        # weworks = WeWork()
        # 实例化Tag类，方便后面调用
        self.tag = Tag()
        self.tag.get_token()

    # 增加标签
    def test_add_tag(self):
        self.tag.add_tag(12)
        list = self.tag.get_tag_list()
        assert list["taglist"][0]["tagname"] == 'UI'

    # 更新标签
    def test_update_tage(self):
        self.tag.update_tag(12)
        list = self.tag.get_tag_list()
        assert list["taglist"][0]["tagname"] == "UI design"

    # 删除标签
    def test_del_tag(self):
        self.tag.delete_tag( 12)
        list = self.tag.get_tag_list()
        assert len(list["taglist"]) == 0

    # 获取标签列表
    def test_tag_list(self):
        list = self.tag.get_tag_list()
