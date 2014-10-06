# coding=utf-8

def formatter(activity_data):
    """
        this is a special formatte r function to be used as a plugin of
        slak-kambanize app
        Process the activitie object and Return the formatted_message for
        this activity
        Arguments:
        @activity_data - dict object with this format:
                        {u'event': u'Task updated',
                         u'text': u'New tag:', u'author': u'mportela'}
        Return the formatted_string for the activity, based in the 'event'
    """
    events_emoji_traslator = {
        u'Task archived': u':+1:',
        u'Assignee changed': u':octocat:',
        u'Comment added': u':speech_balloon:',
        u'Task moved': u':rocket:',
        u'Attachments updated': u':paperclip:',
        u'Task updated': u':pencil:',
        u'Task created': u':ticket:',
        u'External link changed': u':link:',
        u'Tags changed': u':triangular_flag_on_post:'
        }
    emoji = u''
    event = activity_data.get(u'event', u'')
    user = u'*%s*' % activity_data.get(u'author', u'')
    text = activity_data.get(u'text', u'')
    try:
        emoji = u'%s ' % events_emoji_traslator[event]
    except KeyError, e:
        # case of event not know, just return the name with italic format
        event = u'_%s_' % event

    msg = u"%sUsuário: %s Evento: %s"\
          u": %s" % (emoji, user, event, text)

    return msg
