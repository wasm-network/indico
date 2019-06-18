# This file is part of Indico.
# Copyright (C) 2002 - 2019 CERN
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see the
# LICENSE file for more details.

from __future__ import unicode_literals

from indico.core.db.sqlalchemy.descriptions import RenderMode
from indico.core.settings.converters import DatetimeConverter, EnumConverter
from indico.modules.events.settings import EventSettingsProxy
from indico.util.i18n import _
from indico.util.struct.enum import RichEnum


class BOASortField(RichEnum):
    id = 'id'
    abstract_title = 'title'
    board_number = 'board_number'
    session_board_number = 'session_board_number'
    session_title = 'session_title'
    speaker = 'speaker'
    schedule = 'schedule'
    schedule_board_number = 'schedule_board_number'
    session_schedule_board = 'session_schedule_board'


class BOACorrespondingAuthorType(RichEnum):
    none = 'none'
    submitter = 'submitter'
    speakers = 'speakers'


BOASortField.__titles__ = {
    BOASortField.id: _('ID'),
    BOASortField.abstract_title: _('Abstract title'),
    BOASortField.board_number: _('Board Number'),
    BOASortField.session_board_number: _('Session title, Board Number'),
    BOASortField.session_title: _('Session title'),
    BOASortField.speaker: _('Presenter'),
    BOASortField.schedule: _('Schedule'),
    BOASortField.schedule_board_number: _('Schedule, Board Number'),
    BOASortField.session_schedule_board: _('Session, Schedule, Board Number')
}


BOACorrespondingAuthorType.__titles__ = {
    BOACorrespondingAuthorType.none: _('None'),
    BOACorrespondingAuthorType.submitter: _('Submitter'),
    BOACorrespondingAuthorType.speakers: _('Speakers')
}


abstracts_settings = EventSettingsProxy('abstracts', {
    'description_settings': {
        'is_active': True,
        'is_required': True,
        'max_length': None,
        'max_words': None
    },
    'start_dt': None,
    'end_dt': None,
    'modification_end_dt': None,
    'announcement': '',
    'announcement_render_mode': RenderMode.markdown,
    'allow_multiple_tracks': True,
    'tracks_required': False,
    'allow_attachments': False,
    'copy_attachments': False,
    'allow_speakers': True,
    'speakers_required': True,
    'contrib_type_required': False,
    'submission_instructions': ''
}, acls={
    'authorized_submitters'
}, converters={
    'start_dt': DatetimeConverter,
    'end_dt': DatetimeConverter,
    'modification_end_dt': DatetimeConverter
})


abstracts_reviewing_settings = EventSettingsProxy('abstracts_reviewing', {
    'scale_lower': 0,
    'scale_upper': 5,
    'allow_comments': True,
    'allow_convener_judgment': False,  # whether track conveners can make a judgment (e.g. accept/reject)
    'allow_contributors_in_comments': False,
    'reviewing_instructions': '',
    'judgment_instructions': ''
})


boa_settings = EventSettingsProxy('abstracts_book', {
    'extra_text': '',
    'sort_by': BOASortField.id,
    'corresponding_author': BOACorrespondingAuthorType.submitter,
    'show_abstract_ids': False,
    'cache_path': None
}, converters={
    'sort_by': EnumConverter(BOASortField),
    'corresponding_author': EnumConverter(BOACorrespondingAuthorType),
    'announcement_render_mode': EnumConverter(RenderMode)
})
