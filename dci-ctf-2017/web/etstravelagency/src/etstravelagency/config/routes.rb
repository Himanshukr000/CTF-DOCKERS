Rails.application.routes.draw do
  get 'trips' => 'trips#index'

  get 'destinations' => 'destinations#index'

  post 'destinations/book' => 'destinations#book'

  get 'destinations/:id' => 'destinations#show'
end
