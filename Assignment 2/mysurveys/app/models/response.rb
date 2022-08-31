class Response < ApplicationRecord
  
  belongs_to :answer , inverse_of: :responses 

  belongs_to :user , inverse_of: :responses


  has_one :question, :through => :answer

  
  validates :content,
				presence: true

  def to_s
	content
  end

end