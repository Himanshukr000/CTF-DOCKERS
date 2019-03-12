FROM ubuntu:16.04

RUN apt-get update && apt-get -y dist-upgrade

RUN apt-get install -y ruby-dev build-essential patch zlib1g-dev liblzma-dev
RUN gem install bundler

COPY ./etstravelagency/ /etstravelagency

WORKDIR /etstravelagency

RUN bundle install

RUN chown -R www-data:www-data /etstravelagency/tmp

RUN chown root /etstravelagency/flag && chmod 400 /etstravelagency/flag
RUN chmod a+s /etstravelagency/getflag

USER www-data

CMD rails s -e production