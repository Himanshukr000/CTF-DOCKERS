class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  before_action :trips

  protected
  def save_trips
    @trips ||= []
    cookies.signed[:trips] = @trips
  end

  private
  def trips
    cookies.signed[:trips] ||= []
    @trips = cookies.signed[:trips]
  end
end
