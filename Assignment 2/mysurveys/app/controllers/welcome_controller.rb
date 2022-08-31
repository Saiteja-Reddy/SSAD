class WelcomeController < ApplicationController
	before_action :authenticate_user!

  def index
  	@currentUser = current_user.id
  	@currentAdmin = current_user.admin
  	@surveysall = Survey.all
  	@takenall = Taken.all
  end

end
