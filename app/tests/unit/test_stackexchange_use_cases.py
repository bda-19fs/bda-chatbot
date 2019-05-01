import untangle
from bda_core.use_cases.stackexchange.extract_questions_with_answers import (
    extract_questions_with_answers
)


xml = untangle.parse('''
<posts>
  <row Id="1" PostTypeId="1" AcceptedAnswerId="925" CreationDate="2010-07-09T19:07:45.460" Score="59" ViewCount="30457" Body="How old am I?" OwnerUserId="16" LastEditorUserId="41" LastEditDate="2011-08-22T23:44:41.317" LastActivityDate="2018-04-17T23:46:34.353" Title="How can I get chewy chocolate chip cookies?" Tags="&lt;baking&gt;&lt;cookies&gt;&lt;texture&gt;" AnswerCount="11" CommentCount="5" FavoriteCount="23" />
  <row Id="925" PostTypeId="1" CreationDate="2010-07-09T19:08:34.570" Score="29" ViewCount="116927" Body="1993" OwnerUserId="17" LastEditorUserId="41" LastEditDate="2010-11-10T04:44:49.043" LastActivityDate="2015-10-06T21:04:10.933" Title="How should I cook bacon in an oven?" AnswerCount="14" CommentCount="3" FavoriteCount="5" />
</posts>
''')

def test_extract_questions_with_answers():
    extract = extract_questions_with_answers(xml)
    assert extract['questions_answers'] == [
        {
            'answer_id': 925,
            'question': 'How old am I?',
            'answer': '1993',
            'tags': 'baking,cookies,texture'
        }
    ]
