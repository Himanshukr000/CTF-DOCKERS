require 'base64'
require 'openssl'
require 'sinatra'

# Copyright © 2012 Ron Bowes. All Rights Reserved.
# Based off work done by https://github.com/iagox86/poracle

set :bind, '0.0.0.0'
set :port, 10005

@@key = (1..32).map{rand(255).chr}.join

get '/getflag' do
  text = "BSIDES_CTF{9920f5d81fd268fb11fd14bcd2c3df64}\n\nCongrats on getting the flag!\nFor such a top effort you deserve to get a joke - What's a pirate's least favourite letter?\n\nDear Sir,\nWe are writing to you because you have violated copyright ...\n"
  c = OpenSSL::Cipher::Cipher.new("AES-256-CBC")
  c.encrypt
  c.key = @@key

  return (c.update(text) + c.final).unpack("H*")
end

get '/' do
  text = "/getflag to get the flag.<br>/decrypt/&lt;plaintext&gt; to decrypt"
  return text
end

get '/decrypt/' do
  text = "You need to add the ciphertext to decrypt"
  return text
end

get /\/decrypt\/([a-fA-F0-9]+)$/ do |data|
  begin
    data = [data].pack("H*")
    c = OpenSSL::Cipher::Cipher.new("AES-256-CBC")
    c.decrypt
    c.key = @@key
    c.update(data)
    c.final

    return "Yup, I managed to decrypt that....<br>But you have to ask nicely if you want me to give you the value<br><br><br><!--https://www.youtube.com/watch?v=cAstB4KoXXc-->"
  rescue
    return ""
  end
end
