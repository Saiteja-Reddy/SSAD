json.array!(@question.answers) do |answer|
	json.label answer.content.split(':').slice(1..-1).map(&:inspect).join(' ').to_s.gsub('"', '')
	json.value @info[answer.id]
end