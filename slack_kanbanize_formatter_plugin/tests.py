# encoding: utf-8

import unittest
import mock
from ispm_formatter import formatter, _get_flow_msg


class CardFlowTests(unittest.TestCase):
    def test_card_to_peer_review(self):
        text = u"From 'Já detalhados' to 'In Progress.Revis\xe3o Interna'"
        msg = _get_flow_msg(text)
        self.assertEquals(msg, u':mag_right: %s enviou a tarefa para review.')

    def test_started_to_work(self):
        text = u"From 'Já detalhados' to 'In Progress.Fazendo'"
        msg = _get_flow_msg(text)
        self.assertEquals(msg, u':boom: %s começou a trabalhar na tarefa.')

    def test_return_card(self):
        text = u"From 'In Progress.Revis\xe3o externa' to 'In Progress.Fazendo'"
        msg = _get_flow_msg(text)
        self.assertEquals(msg, u':leftwards_arrow_with_hook: %s voltou o card para _Fazendo_.')

    def test_forward_card(self):
        text = u"From 'In Progress.Fazendo' to 'In Progress.Revis\xe3o externa'"
        msg = _get_flow_msg(text)
        self.assertEquals(msg, u':right_arrow: %s avançou o card para _Revisão externa_.')

    def test_column_not_in_flow(self):
        text = u"From 'coluna1' to 'coluna2'"
        msg = _get_flow_msg(text)
        self.assertEquals(msg, u':left_right_arrow: %s moveu o card de _coluna1_ para _coluna2_.')


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

        self.assertEquals(msg, u"")

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

    @mock.patch('ispm_formatter._get_flow_msg')
    def test_change_column(self, flow_msg):
        activity = {
            u'event': u'Task moved',
            u'text': u"From 'Swimlane 1.Column 1' to 'Swimlane 1.Column 2'",
            u'author': u'mportela'
        }

        flow_msg.return_value = '%s changed'

        msg = formatter(activity)

        flow_msg.assert_called_with(activity['text'])


        self.assertEquals(msg, u"*mportela* changed")

    def test_deploy_tag(self):
        activity = {
            u'event': u'Tags changed',
            u'text': u'New tag: empacotado',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u":package: *mportela* gerou pacote com a tarefa.")

    def test_external_link_changed(self):
        activity = {
            u'event': u'External link changed',
            u'text': u'http://google.com',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':link: *mportela* alterou o link do card para http://google.com')

    def test_attachment_added(self):
        activity = {
            u'event': u'Attachments updated',
            u'text': u'arquivo1.gif',
            u'author': u'mportela'
        }

        msg = formatter(activity)

        self.assertEquals(msg,
            u':paperclip: *mportela* alterou os anexos do card: _"arquivo1.gif"_.')

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
