import sublime, sublime_plugin
import os, subprocess

class OpenInIaWriterCommand(sublime_plugin.WindowCommand):
  def get_path(self):
    if self.window.active_view():
      return self.window.active_view().file_name()
    else:
      sublime.status_message(__name__ + ': No file')
      return False

  def is_enabled(self):
    return True

  def run(self, *args):
    print "Opening in iA Writer"
    path = self.get_path()
    if not path:
      return

    subprocess.call(['open', '-a', 'iA Writer', path])
