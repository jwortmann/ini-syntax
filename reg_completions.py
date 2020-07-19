import sublime
import sublime_plugin


class WindowsRegistryCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        pt = locations[0]
        if not view.match_selector(pt, "source.ini | source.reg"):
            return None
        file_name = view.file_name()
        if not file_name or not file_name.lower().endswith("reg"):
            return None
        if pt == len(prefix):
            return [["Windows Registry Editor Version 5.00", "Windows Registry Editor Version 5.00"]]
        elif view.match_selector(pt - len(prefix) - 1, "punctuation.definition.section.begin.ini | meta.section.ini keyword.operator.arithmetic.ini"):
            return (
                [
                    ["HKEY_CLASSES_ROOT", "HKEY_CLASSES_ROOT"],
                    ["HKEY_CURRENT_USER", "HKEY_CURRENT_USER"],
                    ["HKEY_LOCAL_MACHINE", "HKEY_LOCAL_MACHINE"],
                    ["HKEY_USERS", "HKEY_USERS"],
                    ["HKEY_CURRENT_CONFIG", "HKEY_CURRENT_CONFIG"]
                ],
                sublime.INHIBIT_WORD_COMPLETIONS
            )
        return None
