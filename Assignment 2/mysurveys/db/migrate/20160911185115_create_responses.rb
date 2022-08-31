class CreateResponses < ActiveRecord::Migration[5.0]
  def change
    create_table :responses do |t|
      t.text :content
      
      t.references :answer, foreign_key: true
      t.references :user

      t.timestamps
    end
  end
end


