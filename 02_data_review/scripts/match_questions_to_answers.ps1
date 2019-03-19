<#
	.SYNOPSIS
		Matching of questions to answers.
	.DESCRIPTION
		Matches all questions with the corresponding answer.
		The questions and answers have to be in the input csv.
	.PARAMETER dataCsvFilePath
		The csv with the questions and answers.
#>
param(
	[Parameter(Mandatory = $true)]
	$dataCsvFilePath
)

$csv = import-csv $dataCsvFilePath
$questions = @()
$answers = @()
$quest_answ_tuples = @()

#
#	Extracts questions and answers in separate lists.
#
for ($i=0; $i -lt $csv.Length; $i++) {
	$ticket = $csv[$i]
	if ($ticket.creator -eq 3) {
		$questions += $ticket
	} else {
		$answers += $ticket
	}
}

write-host ('number of questions: ' + $questions.Length)
write-host ('number of answers: ' + $answers.Length)


#
#	Creates a tuple of a question and an answer.
#
function createTuple {
	param($question, $answer)
	$tuple = [pscustomobject]@{
		question = $question
		answer = $answer
	}
	return $tuple
}

#
#	Saves each question with the answer in a tuple.
#
for ($i=0; $i -lt $questions.Length; $i++) {
	$quest = $questions[$i]
	$ticketNr = $quest.ticket
	
	for ($j=0; $j -lt $answers.Length; $j++) {
		$answ = $answers[$j]
		if ($ticketNr -eq $answ.ticket) {
			$tuple = createTuple -question $quest -answer $answ
			$quest_answ_tuples += $tuple
		}
	}
}

write-host ('Number of tuples: ' + $quest_answ_tuples.Length)

# Creates the csv header
$resultCsv = "ticket,type,mandant,creator,inquiry,state,meta,answer `n"
# The delimiter for the csv file
$delimiter = ','

#
#	Creates the resulting csv text
#
for ($i=0;$i -lt $quest_answ_tuples.Length;$i++) {
	$tuple = $quest_answ_tuples[$i]
	$quest = $tuple.question
	$answ = $tuple.answer	
	$line = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}" -f $delimiter,$quest.ticket,$quest.type,$quest.mandant,$quest.creator,$quest.inquiry,$quest.state,$quest.meta,$answ.inquiry
	$resultCsv += $line + "`n"
}

$resultCsv | out-file 'questions_answers.csv' -encoding UTF8