# coding=utf-8
import re

FLOW = (
    u'Já detalhados',
    u'In Progress.Fazendo',
    u'In Progress.Revis\xe3o Interna',
    u'In Progress.Revis\xe3o externa',
    u'Entregue',
)

def _get_flow_msg(text):
    from_col, to_col = re.findall("\'(.*?)\'", text, re.U)

    try:
        if FLOW.index(to_col) == 2:
            msg = u':mag_right: %s enviou a tarefa para review.'
            return msg

        if FLOW.index(from_col) == 0 and FLOW.index(to_col) == 1:
            msg = u':boom: %s começou a trabalhar na tarefa.'
            return msg

        if FLOW.index(from_col) > FLOW.index(to_col):
            # avançando tarefa
            base_msg = u':leftwards_arrow_with_hook: %%s voltou o card para _%s_.' % to_col.split('.')[-1]
            return base_msg
        else:
            base_msg = u':right_arrow: %%s avançou o card para _%s_.' % to_col.split('.')[-1]
            return base_msg
    except ValueError:
        return u':left_right_arrow: %%s moveu o card de _%s_ para _%s_.' % (from_col, to_col)


def formatter(activity_data):
    """
        This is a special formatter function to be used as a plugin of
        slak-kanbanize app
        Process the activitie object and Return the formatted_message for
        this activity
        Arguments:
        @activity_data - dict object with this format:
            {u'event': u'Task updated',
            u'text': u'New tag:',
            u'author': u'mportela'}
        Return the formatted_string for the activity, based in the 'event'
    """

    event = activity_data.get(u'event', u'')
    user = u'*%s*' % activity_data.get(u'author', u'')
    text = activity_data.get(u'text', u'')

    if event == u'Assignee changed':
        new_assignee = text.split('New assignee: ')[1]

        if new_assignee == 'None':
            msg = u':runner: %s deixou o card.'

            return msg % user

        # old card owner is intentionally not identified
        msg = u':bust_in_silhouette: %s assumiu o card.' % user

        return msg

    if event == u'Task moved' and\
        u"to 'In Progress.Revis\xe3o Interna'" in text:
        msg = u':mag_right: %s enviou a tarefa para review.'

        return msg % user

    if event == u'Tags changed' and u'New tag: empacotado' in text:
        msg = u':package: %s gerou pacote com a tarefa.'

        return msg % user

    if event == u'Task updated':
        msg = u':pencil: %s atualizou a descrição do card para _"%s"_.'
        
        return msg % (user, text)

    if event == u'External link changed':
        msg = u':link: %s alterou o link do card para %s'
        
        return msg % (user, text)

    if event == u'Attachments updated':
        msg = u':paperclip: %s alterou os anexos do card: _"%s"_.'
        
        return msg % (user, text)

    if event == u'Task created':
        title = text.split('Task ')[1]
        msg = u':o: %s criou o card _"%s"_.'
        
        return msg % (user, title)

    if event == u'Comment added':
        msg = u':speech_balloon: %s comentou no card: _"%s"_.'
        
        return msg % (user, text)

    if event == u'Task moved':
        if text == u'The task was reordered within the same board cell.':
            return ""

        if 'From' in text and 'to' in text:
            return _get_flow_msg(text) % user

    if event == "Task archived":
        title = text.split('Title ')[1]
        msg = u':toilet: %s arquivou o card _"%s"_.'
        
        return msg % (user, title)
        

    # default case
    msg = u":question: Usuário: %s Evento: *%s*"\
          u": _%s_." % (user, event, text)

    return msg
