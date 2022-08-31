class UsersGrid
  include Datagrid

  #
  # Scope
  #
  
  scope do
    User
  end

  #
  # Filters
  #
  
  filter(:id, :string, :multiple => ',')
  filter(:email, :string)
  filter(:condition, :dynamic, :header => "Dynamic condition")
  column_names_filter(:header => "Extra Columns", checkboxes: true)

  #
  # Columns
  #

  column(:id, :mandatory => true)

  column(:email, :mandatory => true) do |model|
    format(model.email) do |value|
      link_to value, "mailto:#{value}"
    end
  end

  column(:actions, :html => true, :mandatory => true) do |record|
    link_to "Delete", "javascript:alert('Oh common! This is demo.')"
  end




end