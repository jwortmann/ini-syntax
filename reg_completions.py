import sublime
import sublime_plugin


class WindowsRegistryCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        pt = locations[0]
        if not view.match_selector(pt, "source.reg"):
            return None
        if pt == len(prefix):
            return ["Windows Registry Editor Version 5.00"]
        elif view.match_selector(pt - len(prefix) - 1, "punctuation.definition.section.begin | meta.section keyword.operator.arithmetic"):
            return (
                [
                    ["HKEY_CLASSES_ROOT\tkey", "HKEY_CLASSES_ROOT"],
                    ["HKEY_CURRENT_USER\tkey", "HKEY_CURRENT_USER"],
                    ["HKEY_LOCAL_MACHINE\tkey", "HKEY_LOCAL_MACHINE"],
                    ["HKEY_USERS\tkey", "HKEY_USERS"],
                    ["HKEY_CURRENT_CONFIG\tkey", "HKEY_CURRENT_CONFIG"]
                ],
                sublime.INHIBIT_WORD_COMPLETIONS
            )
        return None
