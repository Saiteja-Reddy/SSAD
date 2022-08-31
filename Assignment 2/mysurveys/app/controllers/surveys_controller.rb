class SurveysController < ApplicationController

    before_action :authenticate_admin , only: [ :show,:create,:new,:edit , :index , :destroy]
    
  def authenticate_admin
    # TODO Add authentication logic here.
      redirect_to root_url unless current_user.try(:admin)
  end

  def index
    @surveys = Survey.all
  end

  def show
    @survey = Survey.find(params[:id])
  end

  def new
    @survey = Survey.new
  end

  def edit
    @survey = Survey.find(params[:id])
  end

  def create
    @survey = Survey.new(survey_params)
      if @survey.save
        return redirect_to @survey, notice: 'Survey was successfully created.'
      else
        render :new
        return
      end
  end

  def update
    @survey = Survey.find(params[:id])
    @pre = Rails.application.routes.recognize_path(request.referrer)
    @currentUser = current_user.id

    if @pre[:controller] != "takesurvey"
  
      @survey.takens.destroy_all
      @survey.questions.each do |q|
        q.answers.each do |a|
              a.responses.destroy_all
          end
      end

    end

      if @survey.update(survey_params)
        if @pre[:controller] == "takesurvey"
              @taken = Taken.new(user_id: @currentUser , survey_id: @survey.id)
              @taken.save
              return redirect_to controller: 'welcome' , action: 'index' , notice: 'Survey was successfully Taken.' 
        end

        return redirect_to @survey, notice: 'Survey was successfully updated.'
      else
        render :edit
        return
      end
  end

  def destroy
    @survey = Survey.find(params[:id])
    @survey.destroy
    return redirect_to surveys_url, notice: 'Survey was successfully destroyed.'
  end

  private

    def survey_params
      params.require(:survey).permit(:name,questions_attributes: [:id,:content,:_destroy,answers_attributes: [:id,:content,:_destroy,responses_attributes: [:id,:content,:user_id,:_destroy]]])
    end

end
