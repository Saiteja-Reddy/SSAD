class Answer < ApplicationRecord
  
  belongs_to :question ,inverse_of: :answers 

  has_many :responses, inverse_of: :answer , dependent: :destroy

  accepts_nested_attributes_for :responses,allow_destroy: true

  validates :content,
				presence: true
  def to_s
	content
  end

end