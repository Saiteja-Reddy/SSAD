json.array!(@surveys) do |survey|
	json.SurveyName survey.name
	json.SurveyCount @alreadytaken[survey.id]
end