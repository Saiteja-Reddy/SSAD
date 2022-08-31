class TakesurveyController < ApplicationController
	
	def fill
		@survey = Survey.find(params[:id])
		@currentUser = current_user.id
		@taken = Taken.exists?(user_id: @currentUser , survey_id: @survey.id ) ? 1 : 0
		@alreadytaken = Taken.where("survey_id = ?" , @survey.id).all

	end
end
