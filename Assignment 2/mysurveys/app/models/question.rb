class Question < ApplicationRecord
    
    belongs_to :survey ,inverse_of: :questions 
	
   	has_many :answers, inverse_of: :question , dependent: :destroy
	
	accepts_nested_attributes_for :answers,
									reject_if: proc {|attributes| attributes['content'].blank? },
									allow_destroy: true


	validates :content,
				presence: true
	def to_s
		content
	end
end