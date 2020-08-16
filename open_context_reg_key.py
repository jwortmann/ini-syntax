import sublime
import sublime_plugin
import subprocess


class OpenContextRegKeyCommand(sublime_plugin.TextCommand):
    def run(self, edit, event):
        pt = self.view.window_to_text((event["x"], event["y"]))
        regions = self.view.find_by_selector("entity.name.section")
        for region in regions:
            if region.contains(pt):
                reg_key = self.view.substr(region)
                subprocess.call("cmd /c REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Regedit /v LastKey /t REG_SZ /d \"{}\" /f && START regedit".format(reg_key))
                break

    def is_visible(self, event):
        return sublime.platform() == "windows" and self.view.match_selector(self.view.window_to_text((event["x"], event["y"])), "source.reg entity.name.section")

    def want_event(self):
        return True
