class CreateTakens < ActiveRecord::Migration[5.0]
  def change
    create_table :takens do |t|
      t.integer :survey_id
      t.integer :user_id

      t.timestamps
    end
  end
end
