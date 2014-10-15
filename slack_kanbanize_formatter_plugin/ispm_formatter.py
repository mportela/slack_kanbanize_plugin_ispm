# coding=utf-8
import re

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
        msg = u':link: %s alterou o link do card para _"%s"_.'
        
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
        emoji = ':heavy_check_mark:'

        if text == u'The task was reordered within the same board cell.':
            msg = u'%s %s alterou a posição do card.'
            
            return msg % (emoji, user)

        if 'From' in text and 'to' in text:
            from_col, to_col = re.findall("\'(.*?)\'", text, re.U)

            if from_col.split('.')[0] == to_col.split('.')[0]:
                from_col = from_col.split('.')[1]
                to_col = to_col.split('.')[1]

            msg = u"%s %s moveu o card de _%s_ para _%s_."

            return msg % (emoji, user, from_col, to_col)

    if event == "Task archived":
        title = text.split('Title ')[1]
        msg = u':toilet: %s arquivou o card _"%s"_.'
        
        return msg % (user, title)
        

    # default case
    msg = u":question: Usuário: %s Evento: *%s*"\
          u": _%s_." % (user, event, text)

    return msg
