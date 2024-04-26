# Title : GUIDE : Editor
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 25 April 2024

import copy as cpy
import dearpygui.dearpygui as dpg
from Components import Components
from Builder import Builder

class Editor:
    def __init__(self, dataman):
        self.dataman = dataman
        self.designer = None
        self.taggen = dataman.taggen
        self.component_ref = Components()
        self.builder = Builder()
        self.component = None
        self.tag = None

    def updateEditorTab(self):
        self.tag = self.dataman.selected_component
        self.component = cpy.deepcopy(self.dataman.data[self.tag])
        dpg.delete_item("editor_tab", children_only=True)
        with dpg.group(parent="editor_tab"):
            for attr, attr_list in self.component["attributes"].items():
                attr_label = attr_list[0]
                attr_type = attr_list[1]
                attr_default = attr_list[2]