json.(@survey, :id,:name)
json.taken @alreadytaken.size

json.questions @survey.questions do |question|
	json.id question.id
	json.content question.content
	
	json.answers question.answers do |answer|
	json.id answer.id
	json.content answer.content

	json.responses answer.responses do |response|
		json.id response.id
		json.content response.content
		json.user_id response.user_id
	end

	end
end