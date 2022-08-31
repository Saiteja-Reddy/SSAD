class Survey < ApplicationRecord
	
	has_many :questions, inverse_of: :survey , dependent: :destroy

	has_many :takens, inverse_of: :survey , dependent: :destroy

	accepts_nested_attributes_for :questions,
									reject_if: proc {|attributes| attributes['content'].blank? },
									allow_destroy: true

	validates :name,
				presence: true
	def to_s
		name
	end
end