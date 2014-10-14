# encoding: utf-8

import unittest
from ispm_formatter import formatter


class IspmFormatterTests(unittest.TestCase):
    def test_unknow_case(self):
        activity = {
            u'event': u'Untreated event',
            u'text': u'something happened in the board',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':question: Usuário: *mportela* Evento: *Untreated event*: _something happened in the board_.')

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

    def test_change_description(self):
        activity = {
            u'event': u'Task updated',
            u'text': u'nova descrição',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':pencil: *mportela* atualizou a descrição do card para _"nova descrição"_.')

    def test_change_order(self):
        activity = {
            u'event': u'Task moved',
            u'text': u'The task was reordered within the same board cell.',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":heavy_check_mark: *mportela* alterou a posição do card.")

    def test_self_assign(self):
        activity = {
            u'event': u'Assignee changed',
            u'text': u'New assignee: mportela',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":bust_in_silhouette: *mportela* assumiu o card.")

    def test_comment(self):
        activity = {
            u'event': u'Comment added',
            u'text': u'lero lero',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':speech_balloon: *mportela* comentou no card: _"lero lero"_.')

    def test_archive_card(self):
        activity = {
            u'event': u'Task archived',
            u'text': u'Title Tarefa',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':toilet: *mportela* arquivou o card _"Tarefa"_.')

    def test_created_card(self):
        activity = {
            u'event': u'Task created',
            u'text': u'Task nova Tarefa',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':o: *mportela* criou o card _"nova Tarefa"_.')

    def test_change_column_same_lane(self):
        activity = {
            u'event': u'Task moved',
            u'text': u"From 'Swimlane 1.Column 1' to 'Swimlane 1.Column 2'",
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":heavy_check_mark: *mportela* moveu o card de _Column 1_ para _Column 2_.")

    def test_change_column_single_name(self):
        activity = {
            u'event': u'Task moved',
            u'text': u"From 'Column 1' to 'Swimlane 1.Column 2'",
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
           u":heavy_check_mark: *mportela* moveu o card de _Column 1_ para _Swimlane 1.Column 2_.")

    def test_change_column_same_lane(self):
        activity = {
            u'event': u'Task moved',
            u'text': u"From 'Swimlane 1.Column 1' to 'Swimlane 1.Column 2'",
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":heavy_check_mark: *mportela* moveu o card de _Column 1_ para _Column 2_.")

    def test_change_column_different_lanes(self):
        activity = {
            u'event': u'Task moved',
            u'text': u"From 'Swimlane 1.Column 1' to 'Swimlane 2.Column 2'",
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":heavy_check_mark: *mportela* moveu o card de _Swimlane 1.Column 1_ para _Swimlane 2.Column 2_.")

    def _test_(self):
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
