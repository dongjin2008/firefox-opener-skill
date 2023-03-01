from mycroft import MycroftSkill, intent_file_handler
import os


class FirefoxOpener(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('opener.firefox.intent')
    def handle_opener_firefox(self, message):
        self.speak_dialog('opener.firefox')
        try:
            os.system("firefox")
        except:
            self.speak_dialog("error occured while launching firefox")


def create_skill():
    return FirefoxOpener()

