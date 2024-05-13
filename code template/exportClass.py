# Project : App Name
# Author : MyName
# Date : DD/MM/YYYY
# NOTE : Code Generated by GUIDE [https://github.com/tejxpandit/GUI-Designer-DearPyGUI]

import dearpygui.dearpygui as dpg

class GUIDE:
    def __init__(self):
        self.project_name = $PROJECTNAME$
        self.initialize()
        self.createGUI()
        self.runGUI()
        # GUI Variables
        # $PROJECTVARIABLES$

    def initialize(self):
        # Your Preprocess / Init / Main code goes here
        pass

    def createGUI(self, debug=False):
        dpg.create_context()
        dpg.create_viewport(title=self.project_name, width=1200, height=400)
        dpg.set_exit_callback(self.exitProcess)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        # Project GUI
        $PROJECTGUI$
        pass

    def runGUI(self, debug=False):
        if debug:
            ###### For DEBUGGING ######
            dpg.configure_app(manual_callback_management=True)
            while dpg.is_dearpygui_running():
                jobs = dpg.get_callback_queue()
                dpg.run_callbacks(jobs)
                dpg.render_dearpygui_frame()
            ##########################
        else:
            ###### RUN APP ######
            dpg.start_dearpygui()
            #####################
        dpg.destroy_context()