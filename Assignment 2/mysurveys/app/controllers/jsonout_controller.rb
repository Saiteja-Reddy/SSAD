class JsonoutController < ApplicationController

    before_action :authenticate_admin
    
    def authenticate_admin
      # TODO Add authentication logic here.
        redirect_to root_url unless current_user.try(:admin)
    end

	def show
		@survey = Survey.find(params[:id])
		@alreadytaken = Taken.where("survey_id = ?" , @survey.id).all
	end

	def showall
		@surveys = Survey.all
		@alreadytaken = Hash.new()
		@surveys.each do |survey|
			@alreadytaken[survey.id] = (Taken.where("survey_id = ?" , survey.id).all).size
		end
	end

	def index
		@surveys = Survey.all
	end


	def stats
		@survey = Survey.find(params[:id])
		@alreadytaken = Taken.where("survey_id = ?" , @survey.id).all
	end

	def question
		@question = Question.find(params[:id])
		@info = Hash.new()
		@question.answers.each do |answer|
			count = 0
				answer.responses.each do |response|
					if answer.content.split(':')[0] == "radio" 
						if response.content.eql?("1")
							count += 1
						end
					elsif answer.content.split(':')[0] == "check" 
						if response.content.eql?("1")
							count += 1
						end
					end
				end
			@info[answer.id] = count
		end
	end

	def indexusers
    	@users_grid = UsersGrid.new(params[:users_grid]) do |scope|
     		 scope.page(params[:page])
    	end
    	    render :layout => false     

	end

end