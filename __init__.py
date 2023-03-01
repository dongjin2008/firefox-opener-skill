from mycroft import MycroftSkill, intent_file_handler


class FirefoxOpener(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('opener.firefox.intent')
    def handle_opener_firefox(self, message):
        self.speak_dialog('opener.firefox')


def create_skill():
    return FirefoxOpener()

