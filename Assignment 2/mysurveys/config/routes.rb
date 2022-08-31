Rails.application.routes.draw do
  namespace :admin do
    resources :users
resources :answers
resources :questions
resources :responses
resources :surveys
resources :takens

    root to: "users#index"
  end

      resources :surveys

  devise_for :users, :controllers => { :omniauth_callbacks => "callbacks" }

  resources :grids, :only => [:index, :create, :show]


  get 'welcome/index'
  

  root 'welcome#index'

  get 'takesurvey/fill/:id/' => 'takesurvey#fill', :as => 'takesurvey'
 
  get 'jsonout/show/:id/' => 'jsonout#show'
 
  get 'jsonout/showall/' => 'jsonout#showall'

  get 'jsonout/index/' => 'jsonout#index'

  get 'jsonout/stats/:id'  => 'jsonout#stats' , :as => 'stats'

  get 'jsonout/question/:id'  => 'jsonout#question'

  get 'adminpage' => 'jsonout#indexusers' , :as => 'users'


  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
