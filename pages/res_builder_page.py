from pages.__base import BasePage
from elements.__res_builder import BuildLoc
from playwright.sync_api import Page, expect


class Builder(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def load_page(self):
        self.page.goto(BuildLoc.url)

    """Informasi Resume Section"""
    def page_title_presence(self):
        self._look(BuildLoc.page_info_title)
        expect(self._find(BuildLoc.page_info_title)).to_have_text("Buat Resume Terbaikmu")

    def info_resume_title_presence(self):
        self._look(BuildLoc.main_info_title)
        expect(self._find(BuildLoc.main_info_title)).to_have_text("Informasi Resume")

    # Todo 2: Data Diri Section
    # Todo 3: Riwayat Pendidikan Section
    # Todo 4: Riwayat Pekerjaan Section
    # Todo 5: Keahlian
    # Todo 6: Prestasi & Penghargaan
    # Todo 7: Prestasi & Penghargaan
    # Todo 8: Minat
    # Todo 9: Preview
    # Todo 10: Toast Result Action

