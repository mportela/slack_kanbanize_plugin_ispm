# encoding: utf-8

import unittest
from ispm_formatter import formatter


class IspmFormatterTests(unittest.TestCase):
    def test_default_cases(self):
        activity = {
            u'event': u'Comment added',
            u'text': u'teste',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':speech_balloon: Usuário: *mportela* Evento: Comment added: teste')

    def test_assignee_changed_to_none(self):
        activity = {
            u'event': u'Assignee changed',
            u'text': u'New assignee: None',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':runner: *mportela* deixou o card.')

    def test_task_moved_to_peer_review(self):
        activity = {
            u'event': u'Task moved',
            u'text': u"to 'In Progress.Revis\xe3o Interna'",
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":mag_right: *mportela* enviou a tarefa para review.")

    def test_deploy_tag(self):
        activity = {
            u'event': u'Tags changed',
            u'text': u'New tag: empacotado',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":package: *mportela* gerou pacote com a tarefa.")

    def test_(self):
        return
        activity = {
            u'event': u'Assignee changed',
            u'text': u'New assignee: None',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u"")


if __name__ == '__main__':
    unittest.main()
