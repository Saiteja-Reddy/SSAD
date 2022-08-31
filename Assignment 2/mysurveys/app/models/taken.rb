class Taken < ApplicationRecord
	
	  belongs_to :user , inverse_of: :takens 
	  belongs_to :survey , inverse_of: :takens 
	  
end
